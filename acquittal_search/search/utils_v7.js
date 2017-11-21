function get_unicode_length(text) {
    return punycode.ucs2.decode(text).length;
}

function modify_dialog_params(params) {
    if (typeof device_type !== 'undefined' && device_type == 'mobile') {
        var window_width = $(window).width();
        if (window_width < params.width) {
            params.width = 0.95 * window_width;
        }
    }
}

function get_text_length(node) {
     var length = 0;
     var u_len  = 0;
     if(node.nodeType === 3){
         length +=node.nodeValue.length;
         u_len  += get_unicode_length(node.nodeValue)
     } else if(node.nodeType === 1) { // if it is an element node, 
         var children = node.childNodes;    // examine the children
         for(var i = children.length; i--; ) {
             var result = get_text_length(children[i]);
             length += result[0];
             u_len  += result[1];
         }
     }
    return [length, u_len];
}

function get_node_offset(current_node, current_offset, u_offset, divtype) {
    if (current_node.nodeType == 1) {
        var tagName = current_node.tagName;
        var id = current_node.getAttribute("id");
        if (id && (tagName == 'P' || tagName == 'BLOCKQUOTE' || tagName == 'A' || tagName == 'PRE' || ((divtype == 'expanded_headline' || divtype == 'acts') && tagName == 'DIV'))) {
            return [current_node, current_offset, u_offset];
        }
    }
    var prev_sibling = current_node.previousSibling;
    var parent_node  = current_node.parentNode;

    if (prev_sibling) {
        var result = get_text_length(prev_sibling);
        length = result[0];
        u_len  = result[1];
        return get_node_offset(prev_sibling, current_offset + length, 
                               u_offset+ u_len, divtype); 
    } else if (parent_node) {
        return get_node_offset(parent_node, current_offset, u_offset, divtype);
    }
    return null;
}

function is_research_mode() {
    var curr_topic = get_current_topic();
    if (curr_topic.topic_id == "-1") {
        return false;
    }
    return true;
}

function getSelectionText(param) {
    var text = "";
    var startnode_id = "";
    var endnode_id   = "";
    var start_offset = -1;
    var end_offset   = -1;
    var path = [];

    var u_start_offset = -1;
    var u_end_offset   = -1;

    var tid          = param.data.tid;
    var divtype      = param.data.divtype;
    var researchmode = param.data.researchmode;

    if (!is_research_mode()){
        return;
    }

    var curr_topic = get_current_topic();
    var topic      = curr_topic.topic;
    var topics     = get_all_topics();
    
    if (window.getSelection) {
        var sel = window.getSelection();
        if (sel.isCollapsed)
            return; 

        /*
        if (sel.modify) {
            // modify() works on the focus of the selection
            var endNode = sel.focusNode, endOffset = sel.focusOffset;
            sel.collapse(sel.anchorNode, sel.anchorOffset);

            direction = ['forward', 'backward'];

            sel.modify("move", direction[0], "character");
            sel.modify("move", direction[1], "word");
            sel.extend(endNode, endOffset);
            sel.modify("extend", direction[1], "character");
            sel.modify("extend", direction[0], "word");
        }*/
        var range = sel.getRangeAt(0);

        var startContainer = range.startContainer;
        var endContainer   = range.endContainer;

        var startOffset = range.startOffset;
        var endOffset   = range.endOffset;

        // get unicode offset
        var start_text  = startContainer.nodeValue.substring(0, startOffset);
        var u_start_len = get_unicode_length(start_text);

        var end_text  = endContainer.nodeValue.substring(0, endOffset);
        var u_end_len = get_unicode_length(end_text);

        // get offset wrt a know point
        var start_result = get_node_offset(startContainer, startOffset, 
                                           u_start_len, divtype);
        var end_result   = get_node_offset(endContainer, range.endOffset,  
                                           u_end_len, divtype);

        find_path(startContainer, endContainer, path, false);
        if (start_result) {
            startnode_id   = start_result[0].getAttribute("id");
            start_offset   = start_result[1] ;
            u_start_offset = start_result[2];
        }
        if (end_result) {
            endnode_id   = end_result[0].getAttribute("id");
            end_offset   = end_result[1] ;
            u_end_offset = end_result[2];
        }
        text = get_selected_text(startContainer, startOffset, 
                                 endContainer, endOffset, path);
    } else if (document.selection && document.selection.type != "Control") {
        range = document.selection.createRange();
        if (range.text) {
            range.expand("word");
            // Move the end back to not include the word's trailing space(s),
            // if necessary
            while (/\s$/.test(range.text)) {
                range.moveEnd("character", -1);
            }
            range.select();
            text = range.text;
        }
    }

    
    var errmsg = null;

    if (divtype == 'expanded_headline') {
        for (var i = 0; i < path.length; i++) {
            var node = path[i];
            var attr = node.getAttribute('class');
            if (node.nodeType == 1 && node.tagName=='DIV' && attr=='fragment') {
                errmsg = 'Your text selection is not contiguous. It crosses from one fragment to another that are not together in the actual document. So keep your selection limited to just one fragment.';
                break;
            }
        }
    }

    if (startnode_id == "") {
        errmsg = 'The start of the selection is outside the permitted range. Reduce it to the text with in the document and do not try to include titles etc.';
    }

    if (endnode_id == "") {
        errmsg = 'The end of the selection is outside the permitted range. Reduce it to the text with in the document and do not try to include anything else.';

    }

    if (errmsg)     {
        err_new_note(topic, errmsg);
    } else {
        new_note_dialog(startnode_id, endnode_id, start_offset, end_offset, 
                        u_start_offset, u_end_offset, text, tid, topics);
    }    
}

function err_new_note(topic, errmsg) {
    var newDiv = $("<div></div>"); 
    newDiv.html('<div class="annotate">' + errmsg + '</div>');
    var params = {title: topic,  closeText: "", width: 450}; 
    modify_dialog_params(params);
    $(newDiv).dialog(params)
}

function new_note_dialog(startnode_id, endnode_id, start_offset, end_offset, 
                         u_start_offset, u_end_offset, text, tid, topics) {
    var newDiv = $("<div></div>");
    var trimmed_doctext = trim_doctext(text);

    var topic_html = '<div class="note_topic">Topic<select name="note_topic" class="note_topic_select">';
    for (var i = 0; i < topics.length; i++) {
        var topic = topics[i];

        var selected = '';
        if (topic.checked) {
            selected = ' selected="selected"';
        }

        topic_html += '<option value="' + topic.topic_id + '"' + selected + '>' + topic.topic + '</option>\n';
    }

    topic_html += '</select></div>';

    newDiv.html(topic_html + '<textarea  name="note" class="research_comment" placeholder="Add a comment (optional)"></textarea><pre class="annotate">' + trimmed_doctext + '</pre>');
    var save_button = {
        text: "Save",
        click: function(e) {
            var note = $(this).children("textarea")[0].value;
            var obj = $(this).find("select[name='note_topic'] option:selected");
            var topic_id = get_select_value(obj);

            data = {"startnode_id"  : startnode_id,
                    "endnode_id"    : endnode_id,
                    "start_offset"  : start_offset, 
                    "end_offset"    : end_offset, 
                    "u_start_offset": u_start_offset, 
                    "u_end_offset"  : u_end_offset, 
                    "text"          : text,
                    "topic_id"      : topic_id,
                    "note"          : note}; 
            // here is the modification of the button
            // opacity set to 25%, all events unbound
            $(e.target).css({opacity: 0.25});
            $(e.target).attr('disabled', 'true');
                                 
            $.ajax({type:"post", 
                    url: "/research/savenote/" + tid + "/",
                    dataType: 'json', 
                    data: data})
             .done(function (data, textStatus, jqXHR) {
                 $(newDiv).dialog("close");
                 if(apply_note(data)) {
                     add_to_rightnav(data);
                     create_note_button(get_dialog_selector(data));
                 }
                 add_tooltip(data);
             })
             .fail(function ( jqXHR, textStatus, errorThrown )  {
                 newDiv.html("Sorry an error occurred. " + jqXHR.responseText);
             });
        }
    };

    var disable_research = {
        text: 'Disable research?', 
        click: function(e) {
            $(newDiv).dialog("close");
            disable_research_box(e);
        }
    };

    var params =  {title: 'New note',  closeText: "", width: 450, 
                   buttons: [disable_research, save_button]};
    modify_dialog_params(params);
    $(newDiv).dialog(params);

}

function disable_research_box (e) {
    var newDiv = $("<div></div>");
    newDiv.html('If you disable research mode, the note taking will not pop up anymore. You can enable the research mode again by changing to a topic in the dashboard below. Do you want to disable the research?');
    var yes_button = {
        text: "Yes", 
        icons: {secondary: 'ui-icon-check'}, 
        click: function(e) {
            $.ajax({type:"post",
                    url: "/research/chtopic/",
                    data: {'topic_id': -1}})
             .done(function () {
                $(newDiv).dialog("close");
                 fetchLatestTopics();
            })
            .fail(function () {
                 newDiv.html("Sorry, got an error in disabling research. Try after sometime.");
            });
        }
    };

    var no_button = {
        text: "No",
        icons: {secondary: 'ui-icon-close'}, 
        click: function(e) {
            $(newDiv).dialog("close");
        }

    };

    params = {title: 'Disable research?',  closeText: "", width: 450,
              buttons: [no_button, yes_button]};
    modify_dialog_params(params);
    $(newDiv).dialog(params);

}

function add_note(e) {
    var newDiv  = $("<div></div>"); 
    var buttons  = []
    var topic_id = $(e.target).attr('id').split('_')[1];

    var save_button = {
        text: "Save",
        click: function(e) {
            var target   = $(e.target);
            target.css({opacity: 0.25});
            target.attr('disabled', 'true');

            var note = $(this).children("textarea")[0].value;

            $.ajax({type:"post", 
                url: "/research/addto/",
                dataType: 'html', 
                data: {note: note, topic_id: topic_id, need_resp: 't'} })
            .done(function (data, textStatus, jqXHR) {
                $(newDiv).dialog("close");
                $("#topic_notes").prepend(data);
             })  
             .fail(function ( jqXHR, textStatus, errorThrown )  {
                 newDiv.html("Sorry an error occurred. " + jqXHR.responseText);
             });  
         }    
    };
    buttons.push(save_button);

    newDiv.html('<textarea  name="note" class="research_comment" placeholder="Add facts or comments about the topic"></textarea>')
    var topic    = get_topic($(e.target));

    var params = {title: topic,  closeText: "", width: 450, buttons: buttons};
    modify_dialog_params(params);
    $(newDiv).dialog(params);
}

function fetchLatestTopics() {
    $.get( "/research/latesttopics/", function( data ) {
        $( "#research_search").html(data);
        $("input[type=radio][name=topic_id]").change(chtopic);
        $("#rmtopic_b").click(rmtopic);
        hoverHighlight();
    });
}

function get_current_topic() {
    var obj = $("input[name='topic_id']:checked");
    var topic_id = obj.attr('value');
    var topic = 'Non research mode';

    if (topic_id != "-1") {
        topic  = obj.next('a').text();
    }
    return {'topic_id': topic_id, 'topic': topic};
}
function get_all_topics() {
    var topics     = [];

    $("input[name='topic_id']").each(function(index) {
        var obj   = $(this);
        var topic_id = obj.attr('value');
        if (topic_id != "-1") {
            var topic  = obj.next('a').text();
            topics.push({'topic': topic, 'topic_id': topic_id, 'checked': obj.is(":checked")}); 
        }
    });
    return topics;
}


function hoverHighlight()  {
    var obj = $('#hover_slider');
    obj.switchButton({
        on_label: 'Always',
        off_label: 'On hover'
    });
    if (obj.is(":checked")) {
        addNoteHighlights();
    }
    obj.change(function (e) {
        var val =  $(e.target).is(":checked");
        if (val) {
            val = 1;
        } else {
            val = 0;
        }
        if (val == 1){
            addNoteHighlights();
        } else {
            removeNoteHighlights();
        }

        $.ajax({type:"post", 
                url: "/research/chhover/",
                dataType: 'json', 
                data: {'hover': val}  });


    });
}
function queryMonitoring()  {
    var obj = $('.query_monitor');
    obj.switchButton({
        on_label: 'Yes',
        off_label: 'No'
    });
    obj.change(function (e) {
        var qid =  $(e.target).attr("data-queryid");

        $.ajax({type:"post", 
                url: "/research/toggle_qwatch/",
                data: {'qid': qid} });

    });
}

function addNoteHighlights() {
    $('.research_note').addClass('highlight_notes');
    $('.note_fragment').addClass('highlight_notes');
}

function removeNoteHighlights() {
    $('.research_note').removeClass('highlight_notes');
    $('.note_fragment').removeClass('highlight_notes');
}

function fetchNote(param) {
    var note_id = param.note_id;

    $.getJSON( "/research/onenote/" + note_id + "/", function( note ) {
            apply_note(note);
            create_note_button(get_dialog_selector(note));
            add_tooltip(note);
    });

}

function no_research_dialog() {
    var params = {title: "Non research mode",   closeText: "", width: 450};
    modify_dialog_params(params);
    var newDiv = $("<div></div>"); 
    newDiv.html('You are currently in a non research mode. Select a topic from the dashboard below to start research.');
    $(newDiv).dialog(params);
}

function add_to_research(e) {
    if (!is_research_mode()) {
        no_research_dialog();
        return;
    }
    var search_query = e.data.search_query;
    
    var target = $(e.target);
    var tid    = target.attr('id').split('_')[1];

    var parentNode = target.parent().parent();
    var children = parentNode.children('.headline');
    var headline = children.text();
    $.ajax({type: 'post', 
           url: '/research/addto/',
           data: {'tid': tid, 'note': search_query, 'text': headline}
    }).done(function() {
        target.unbind();
        target.html('Added');
        target.removeClass('add_research');
        target.addClass('research_added');
    });
}

function add_fragment(e) {
    if (!is_research_mode()) {
        no_research_dialog();
        return;
    }
    
    var target = $(e.target)
    var button = target.parent();
    var tid    = button.attr('data-tid');
    var note   = button.attr('data-query');

    var parentNode = button.parent().parent();
    var children = parentNode.children('.query_fragment');
    var headline = children.text();
    $.ajax({type: 'post', 
           url: '/research/addto/',
           data: {'tid': tid, 'note': note, 'text': headline}
    }).done(function() {
        target.unbind();
        button.removeClass('add_fragment');
        button.addClass('added_fragment');
        button.button('option', 'label', 'In research');
        button.button('option', 'icons', {secondary: 'ui-icon-star'}); 
    });
}


var max_note_len = 25;

function get_note_link_id(id) {
    return "notelink_" + id;
}

function get_note_desc(note) {
    var note_desc = note.note;
    if (!note_desc) {
        note_desc = note.doctext;
     }

     if (note_desc.length > max_note_len) {
         note_desc = note_desc.substring(0, max_note_len) + '...';
     } else if (!note_desc) {
         note_desc = 'No Comment';
     }
     return note_desc;
}

function get_note_link(note) {
    var note_desc = get_note_desc(note);
    var id        = get_note_link_id(note.id);

    var href_id   = '#note_' + note.id;
    return '<a href="' + href_id+ '" id="' + id + '">' + note_desc + '</a>';

}

function update_note_link(note) {
    var link_id = get_note_link_id(note.id);
    var link    = get_note_link(note);
    $('#' + link_id).replaceWith(link);
}

function get_note_rightnav(note) {
    var note_html = get_note_link(note);
    return '<div class="note_desc">' + note_html + '</div>';
}

function add_to_rightnav(note) {
    var note_html = get_note_rightnav(note);
    $('#notes_right').append(note_html);
}

function create_note_button(selector) {
    $(selector).button({
        text: false, 
        icons: {primary: 'ui-icon-comment'}
    });
}

// Read a page's GET URL variables and return them as an associative array.
function getUrlVars()
{
    var vars = [], hash;
    var hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
    for(var i = 0; i < hashes.length; i++)
    {
        hash = hashes[i].split('=');
        vars.push(hash[0]);
        vars[hash[0]] = hash[1];
    }
    return vars;
}

function fetchNotes(param) {
    var tid     = param.tid;
    var topicid = param.topicid;

    var notesUrl = "/research/notes/" + tid + "/";
    if (topicid  != null) {
        notesUrl = notesUrl + '?topicid=' + topicid;
    }

    $.getJSON(notesUrl, function( data ) {
        var html = ''
        $.each(data, function(noteIndex, note) {
            if(apply_note(note)) {
                html += get_note_rightnav(note);
            }
        });

        $('#notes_right').html(html);
        create_note_button('.ikimg');

        $.each(data, function(noteIndex, note) {
            add_tooltip(note);
        });
    });
}

function delete_note(note) {
    var note_id = "note_" + note.id;
    var span = document.getElementById(note_id);
    delete_element(span);

    for (var counter = 1; counter < note.pos; counter ++) {
        span = document.getElementById(note_id + '-' + counter);
        delete_element(span);
    }
    $('a[href="#' + note_id + '"]').remove();
}

function delete_element(element) {
    var parentNode = element.parentNode; 
    if (element == null || parentNode == null) {
        return false;
    }
    while(element.firstChild) {
        var child = element.removeChild(element.firstChild);
        if (child.nodeType == 1 && child.tagName == 'SPAN') {
            var span_class = child.getAttribute('class');
            if (span_class && span_class.indexOf('ikimg') >= 0) {
                continue;
            }
        }

        parentNode.insertBefore(child, element);
    }
    parentNode.removeChild(element);
    return true;
}

var max_doctext_len = 500;

function trim_doctext(doctext) {
    if (doctext.length > max_doctext_len) {
        return doctext.substr(0, max_doctext_len) + ' ...';
    } 
    return escapeHtml(doctext);
}
function delete_note_box(note, del) {
    var newDiv = $("<div></div>"); 

    var note_html = ''

    if (note.note) {
        note_html += '<div class="research_comment_del">' + note.note + '</div>';
    } else if (note.doctext) {
        note_html += '<div class="doctext">' + trim_doctext(note.doctext) + '</div>';
    }

    newDiv.html(note_html);
    var buttons = []
    var yes_button = {
        text: "Yes", 
        icons: {secondary: 'ui-icon-check'}, 
        click: function(e) {
            $.ajax({type:"post", 
                    url: "/research/delnote/" + note.id + "/"})
            .done(function (data, textStatus, jqXHR) {
                if (del) {
                     delete_note(note);
                } else {
                    location.reload();
                }
                $(newDiv).dialog("close");
            })
            .fail(function () {
                 newDiv.html("Sorry, got an error in deleting the comment. Try after sometime.");
            });
        }    
    };
    var no_button = {
        text: "No",
        icons: {secondary: 'ui-icon-close'}, 
        click: function(e) {
            $(newDiv).dialog("close");
        }


    };
            
    buttons.push(no_button);
    buttons.push(yes_button);

    var params = {title: "Do you really want to delete this comment?",  
                      closeText: "", width: 450, buttons: buttons};
    modify_dialog_params(params);
    $(newDiv).dialog(params);
}


function deltopic_box(topic, topic_id) {
    var newDiv = $("<div></div>"); 

    newDiv.html('<div>' + topic + '</div>');
    var buttons = []
    var yes_button = {
        text: "Yes", 
        icons: {secondary: 'ui-icon-check'}, 
        click: function(e) {
            $.ajax({type:"post", 
                    url: "/research/deltopic/" + topic_id + "/"})
            .done(function (data, textStatus, jqXHR) {
                $(newDiv).dialog("close");
                window.location = '/members/';
            })
            .fail(function () {
                 newDiv.html("Sorry, got an error in deleting the topic. Try after sometime.");
            });
        }    
    };
    var no_button = {
        text: "No",
        icons: {secondary: 'ui-icon-close'}, 
        click: function(e) {
            $(newDiv).dialog("close");
        }

    };
            
    buttons.push(no_button);
    buttons.push(yes_button);

    var params = {title: "Do you really want to delete this topic?",  
                  closeText: "", width: 450, buttons: buttons};
    modify_dialog_params(params);
    $(newDiv).dialog(params);
}

function modnote_on_topic(e) {
    e.preventDefault();
    var note_id = $(e.target).attr('id').split('_')[1];


    $.getJSON( "/research/onenote/" + note_id + "/", function( note ) {
        note_dialog_box(note, false);
    });
}

function note_dialog(param) {
    var note   = param.data.note;
    var del    = param.data.del;

    param.stopPropagation();
    param.preventDefault();
    note_dialog_box(note, del);
}

function note_del_button(newDiv, note, del) {
    var del_button =  {
        text: "Delete It!",
        icons: {secondary: 'ui-icon-closethick'}, 
        click: function(e) {
            $(newDiv).dialog("close");
            delete_note_box(note, del);
        }
    }
    return del_button;

}

function rmnote_topic_button(newDiv, note, currtopic_id) {
    var rmnote_button =  {
        text: "Remove from topic",
        icons: {secondary: 'ui-icon-closethick'}, 
        click: function(e) {
            $(e.target).css({opacity: 0.25}).unbind();

            $.ajax({type:"post", 
                    url: "/research/rmnote/" + currtopic_id + "/", 
                    data: {'note_id': note.id}})
            .done(function (data, textStatus, jqXHR) {
                $(newDiv).dialog("close");
                 location.reload();
            })
            .fail(function () {
                 newDiv.html("Sorry, got an error in updating the comment. Try after sometime.");
            });
        }
    }
    return rmnote_button;
}

function note_update_button(newDiv, note, del) {
    var update_button = {
        text: "Update",
        icons: {secondary: 'ui-icon-arrowrefresh-1-e'}, 
        click: function(e) {
            comment = $(this).children("textarea")[0].value;
            $(e.target).css({opacity: 0.25}).unbind();

            $.ajax({type:"post", 
                    url: "/research/updatenote/" + note.id + "/", 
                    dataType: 'json', 
                    data: {'note': comment}})
            .done(function (data, textStatus, jqXHR) {
                if (del) {
                    detach_tooltip(data);
                    detach_note_dialog(data);
                    attach_note_dialog(data);
                    attach_tooltip(data);
                    update_note_link(data);
                    $(newDiv).dialog("close");
                } else {
                    location.reload();
                }
            })
            .fail(function () {
                 newDiv.html("Sorry, got an error in updating the comment. Try after sometime.");
            });
        }

    };

    return update_button;
}

function note_dialog_box(note, del) {
    var newDiv = $("<div></div>"); 

    var html_content = '';
    if (note.modifiable) {
        html_content += '<textarea  name="note" class="research_comment">' + note.note + '</textarea>';
    } else {    
        html_content += '<div class="note_unmod">' + note.note + '</div>';
    }

    if (note.doctext) {
        html_content += '<pre class="annotate">' + trim_doctext(note.doctext) + '</pre>';
    }

    if (note.user) {
        var uniqname = note.user.uniqname;
        var username = note.user.name;

        html_content += '<div class="note_author">by <a href="/research/notes/' + uniqname +'/">' + username + '</a></div>';
    }

    newDiv.html(html_content );


    var curr_topic    = get_current_topic();
    var topic         = note.topic; 
    var topic_ids     = note.topic_ids
    var curr_topic_id = parseInt(curr_topic.topic_id);
 
    var buttons = [];
    if (curr_topic_id != note.topic_id && curr_topic_id != -1 &&  topic_ids.indexOf(curr_topic_id)>= 0) {
        buttons.push(rmnote_topic_button(newDiv, note, curr_topic_id));
    } else if (note.modifiable) {
            buttons.push(note_del_button(newDiv, note, del));
    }

    if (note.modifiable) {
        buttons.push(note_update_button(newDiv, note, del));
    }

    var add_to_research = null;

    if (curr_topic_id == -1) {
        add_to_research = {text: 'Research disabled', disabled: true};
    } else if (curr_topic_id == note.topic_id || topic_ids.indexOf(curr_topic_id)>= 0){        
        add_to_research = {text: 'In current topic', disabled: true};
    } else {
        add_to_research = {
            text: 'Add to current topic', 
            icons: {secondary: 'ui-icon-plusthick'}, 
            click: function(e) {
                $(e.target).css({opacity: 0.25}).unbind();

                $.ajax({type:"post", 
                        dataType: 'json', 
                        url: "/research/addtocurrent/" + note.id + "/"})
                .done(function (data, textStatus, jqXHR) {
                    if (del) {
                        detach_note_dialog(data);
                        attach_note_dialog(data);
                    }
                    $(newDiv).dialog("close");
                })
                .fail(function () {
                   newDiv.html("Sorry, got an error while adding the comment. Try after sometime.");
                });

            }
        };

    }
    if (!note.is_public) {
        buttons.push(add_to_research);
    }

    params = {title: topic,  closeText: "", width: 450, buttons: buttons};
    modify_dialog_params(params);
    $(newDiv).dialog(params);

}

function get_dialog_selector(note) {
    var note_id = 'note_' + note.id;
    return 'span[id="' + note_id + '_img"]';
}

function detach_note_dialog(note) {
    var note_selector = get_dialog_selector(note); 
    $(note_selector).unbind();
}

function attach_note_dialog(note) {
    var note_selector = get_dialog_selector(note); 
    $(note_selector).bind('click', {note: note, del: true}, note_dialog);
}

function get_tooltip_selector(note) {
    var note_id = 'note_' + note.id;
    return 'span[id|="' + note_id + '"]';
}

function detach_tooltip(note) {
    var note_selector = get_tooltip_selector(note);
    $(note_selector).tooltip("destroy");
}


function escapeHtml(str) {
    var div = document.createElement('div');
    div.appendChild(document.createTextNode(str));
    return div.innerHTML;
}

function attach_tooltip(note) {
    var position = { my: "left top", at: "right top", collision: "flipfit" };
    var note_selector = get_tooltip_selector(note);

   $(note_selector).tooltip({content: escapeHtml(note.note), 
                             tooltipClass: 'note_tooltip',
                             items: note_selector, position:position});


}

function add_tooltip(note) {
    attach_tooltip(note);
    attach_note_dialog(note);

    var note_id = 'note_' + note.id;
    var note_spans = [note_id];
    for (var count = 1; count < note.pos; count++) {
        var new_span = note_id + '-' + count;
        note_spans.push(new_span);
    }
    if (note_spans.length > 1) {
        add_hover(note_spans);
    }

    var hover_button = $('#hover_slider');
    if (hover_button.length == 0 || hover_button.is(":checked")) {
        addNoteHighlights();
    }
}

function change_background_on_hover(init_id, receiver_id) {
    $('#' + init_id).hover(
        function () { 
            $('#'+ receiver_id).css('background-color', '#E0F4FF');
        }, 
        function () { 
            $('#'+ receiver_id).css('background-color', '');
        });
}

function add_hover(note_spans) {
    for (var i = 0; i < note_spans.length; i ++) {
        for (var j = 0; j < note_spans.length; j++) {
            if (i!= j) {
                change_background_on_hover(note_spans[i], note_spans[j]);
            }
        }
    }
}

function find_text_node(node, offset, reverse){
    if (node == null) {
        return null;
    }

    if (node.nodeType == 3) {
        if (offset < node.nodeValue.length) {
            return [node, offset];
        } else {
            var nextSibling = node.nextSibling;
            var parentNode  = node.parentNode;

            offset = offset - node.nodeValue.length;

            var nextNode = null;
            var reverse  = false;

            if (nextSibling != null) {
                nextNode = nextSibling;
            } else if (parentNode != null) {
                nextNode = parentNode;
                reverse = true;
            }
            return find_text_node(nextNode, offset, reverse);
        } 
    } else{
        var nextReverse  = false;
        var nextNode = null;

        if (reverse) {
            var nextSibling = node.nextSibling;
            var parentNode  = node.parentNode;

            if (nextSibling != null) {
                nextNode = nextSibling;
            } else {
                nextNode = parentNode;
                nextReverse = true;
            }


        } else {
            if (node.firstChild) {
                nextNode = node.firstChild;
            } else if (node.nextSibling) {
                nextNode = node.nextSibling;
            } else {
                nextNode = node.parentNode;
                nextReverse = true;
            }
        }

        return find_text_node(nextNode, offset, nextReverse);
    }
    return null;
}

function inline_tag(tagName) {
    if (tagName == 'P' || tagName == 'PRE' ||tagName == 'BLOCKQUOTE' 
                    || tagName == 'DIV')  {
        return false;
    } 
    return true;
}

function inline_node(node) {
    if (node.nodeType == 3) {
        return true;
    } else if (node.nodeType == 1 && inline_tag(node.tagName)) {
        return true;
    }
    return false;
}

function wordbreak_tag(tagName) {
    if (tagName == 'SPAN' || tagName == 'FONT'  || tagName ==  'Q' || tagName == 'OBJECT' || tagName == 'BDO' || tagName == 'SUB' || tagName == 'SUP' || tagName == 'CENTER' || tagName == 'B' || tagName == 'I' || tagName == 'EM' || tagName ==   'BIG' || tagName == 'SMALL' || tagName == 'A' || tagName == 'TT')
        return false;
    return true;     
}

function wordbreak_node(node) {
    if (node.nodeType == 3) {
        return false;
    } else if (node.nodeType == 1 && wordbreak_tag(node.tagName)) {
        return true;
    }
    return false;

}

function normalize_spaces(s) {
    return s.replace(/\s+/g, ' ');
}

function is_within_pre(node) {
    while (node != null) {
        var tagName = node.tagName;
        if (tagName == 'PRE') {
            return true;
        } else if (tagName == 'P' || tagName == 'DIV' || tagName == 'BLOCKQUOTE') {
            return false;
        }
        node = node.parentNode;
    }
    return false;
}

function get_text_between(currentNode, endNode, startOffset) {
    var text    = '';
    var reverse = false;
    var normalize = !is_within_pre(currentNode);

    while (currentNode != endNode) {        
        if (currentNode.nodeType == 3) {
            var s = currentNode.nodeValue;
            if (startOffset > 0) {
                s = currentNode.nodeValue.substring(startOffset);
                startOffset = 0;
            }
            if (normalize) {
                text += normalize_spaces(s);
            } else {
                text += s;
            }
        }
        
        var firstChild  = currentNode.firstChild;
        var nextSibling = currentNode.nextSibling;
        var parentNode  = currentNode.parentNode;
        if (reverse) {
            if (nextSibling != null) {
                currentNode = nextSibling;
                reverse = false;
            } else {
                currentNode = parentNode;
                if (normalize && currentNode.tagName == 'PRE') {
                    normalize = false;
                }
            }

        } else {
            if (firstChild != null) {
                normalize = currentNode.tagName != 'PRE';

                if (!inline_node(currentNode)) {
                    text += '\n\n';
                } 

                currentNode = firstChild;
                reverse = false;
            } else if (nextSibling != null) {
                currentNode = nextSibling;
                reverse = false;
            } else {
                currentNode  = currentNode.parentNode;
                if (normalize && currentNode.tagName == 'PRE') {
                    normalize = false;
                }
                reverse = true;
            }
        }
    }
    return text;
}


function get_selected_text(startNode, startOffset, endNode, endOffset, path) {
    if (startNode == endNode) {
        var normalize = !is_within_pre(startNode);
        var s = startNode.nodeValue.substring(startOffset, endOffset);
        if (normalize) {
            s = normalize_spaces(s);
        }
        return s;
    }

    var text = get_text_between(startNode, endNode, startOffset);
    var normalize = !is_within_pre(endNode);
    var s = endNode.nodeValue.substring(0, endOffset);

    if (normalize) {
        s = normalize_spaces(s);
    }

    text += s;
    return text;
}

function find_path(currentNode, endTextNode, path, reverse) {
    if (currentNode == null) {
        return false;
    } else if (currentNode === endTextNode) {
        return true;
    } else if (reverse) {
        var nextSibling = currentNode.nextSibling;
        var parentNode  = currentNode.parentNode;

        var reverse     = false;
        var nextNode    = null;

        if (nextSibling) {
            nextNode = nextSibling ;
        } else if (parentNode) {
            nextNode = parentNode;
            reverse  = true;
        }

        if (path.length > 0) {
            var lastNode = path.pop();
            if (lastNode != currentNode || !inline_node(lastNode)){
                path.push(lastNode);
            }
        }

        return find_path(nextNode, endTextNode, path, reverse);

    } else {
        var firstChild  = currentNode.firstChild;
        var nextSibling = currentNode.nextSibling;
        var parentNode  = currentNode.parentNode;

        var reverse     = false;
        var nextNode    = null;

        if (firstChild && currentNode.nodeType == 1) {
            path.push(currentNode);
        }

        if (firstChild) {
            nextNode = firstChild;
        } else if (nextSibling) {
            nextNode = nextSibling;
        } else if (parentNode) {
            nextNode = parentNode;
            reverse = true;
        }
        return find_path(nextNode, endTextNode, path, reverse);
    }
    return false;
}

function get_new_span(note) {
    var span       = document.createElement("span");

    var id = "note_" + note.id;

    if (note.pos) {
        id = id + "-" + note.pos;
        note.pos += 1;
        span.setAttribute("class", "note_fragment");
    } else {
        note.pos = 1;
        span.setAttribute("class", "research_note");
        var span_img = document.createElement("span");
        span_img.setAttribute("class", "ikimg");
        span_img.setAttribute("id", id + "_img");
        span.appendChild(span_img);
    }
    
    span.setAttribute("id", id);
    return span;
}
function apply_note(note) {
     var startOffset = note.startoffset;
     var endOffset   = note.endoffset;

     var startnode = document.getElementById(note.startnode);
     var endnode   = document.getElementById(note.endnode);

     if (startnode == null || endnode == null) {
         return false;
     }

     var start = find_text_node(startnode, startOffset, false);
     var end   = find_text_node(endnode, endOffset, false)

     if (start == null || end == null) {
         return false;
     }

     var startTextNode = start[0];
     var endTextNode   = end[0]

     startOffset = start[1];
     endOffset   = end[1];

     var parentNode = startTextNode.parentNode;
     if (startTextNode === endTextNode) {
         var span = get_new_span(note);

         if (startOffset == 0 && endOffset == endTextNode.nodeValue.length -1) {
             parentNode.replaceChild(span, startTextNode);
             span.appendChild(startTextNode);
         } else  if (startOffset > 0) {
             var leftText  = startTextNode.nodeValue.substring(0, startOffset);
             var leftNode  = document.createTextNode(leftText);

             var midText  = startTextNode.nodeValue.substring(startOffset, endOffset);
             span.appendChild(document.createTextNode(midText));

             if (endOffset < endTextNode.nodeValue.length -1) {
                 var rightText  = startTextNode.nodeValue.substring(endOffset);
                 var rightNode  = document.createTextNode(rightText);
                 parentNode.replaceChild(rightNode, startTextNode);
                 parentNode.insertBefore(span, rightNode);
             } else {
                 parentNode.replaceChild(span, startTextNode);
             }
             parentNode.insertBefore(leftNode, span);
         }   else {
             var rightText  = startTextNode.nodeValue.substring(endOffset);
             var rightNode  = document.createTextNode(rightText);


             var midText  = startTextNode.nodeValue.substring(0, endOffset);
             span.appendChild(document.createTextNode(midText));

             parentNode.replaceChild(rightNode, startTextNode);
             parentNode.insertBefore(span, rightNode);
         }

     } else {
         var path = []
         var currentNode = startTextNode.nextSibling;
         var reverse     = false;

         if (currentNode == null) {
             currentNode = startTextNode.parentNode;
             reverse     = true;
         }
         var retval = find_path(currentNode, endTextNode, path, reverse);
         if (!retval) {
             return false;
         }

         var span = get_new_span(note);
         var nextNode = startTextNode.nextSibling;

         if (startOffset > 0) {
             var leftText  = startTextNode.nodeValue.substring(0, startOffset)
             var rightText = startTextNode.nodeValue.substring(startOffset);

             span.appendChild(document.createTextNode(rightText));
             leftNode  = document.createTextNode(leftText);
             parentNode.replaceChild(span, startTextNode);
             parentNode.insertBefore(leftNode, span);
         } else {
             startTextNode = parentNode.replaceChild(span, startTextNode);
             span.appendChild(startTextNode);
         }

         if (nextNode == null ) {
             while (parentNode.nextSibling == null) {
                 parentNode = parentNode.parentNode;
             }
             var span = get_new_span(note);
             nextNode = parentNode.nextSibling;
             parentNode.parentNode.insertBefore(span, nextNode);
         }
         return traverse_and_insert(note, span, nextNode, path, 0, endTextNode, endOffset);
     }
     return true;
}

function traverse_and_insert(note, span, currentNode, path, pos, endNode, endOffset) {
    if (currentNode == endNode) {
        var parentNode = endNode.parentNode;
        if (endOffset < endNode.nodeValue.length -1) {    
            var rightText =  endNode.nodeValue.substring(endOffset);
            var leftText  =  endNode.nodeValue.substring(0, endOffset);
            span.appendChild(document.createTextNode(leftText));
            parentNode.replaceChild(document.createTextNode(rightText), endNode);
        } else if (endOffset > 0) {
            var textNode = parentNode.removeChild(endNode); 
            span.appendChild(textNode);
        }
        return true;
    } else {
        var nextSibling = currentNode.nextSibling;
        var firstChild  = currentNode.firstChild;
        var parentNode  = currentNode.parentNode;

        var blockNode = null;

        if (pos < path.length) {
            blockNode = path[pos];
        }  

        if (currentNode === blockNode) {
            var span = get_new_span(note);
            var fChild = currentNode.firstChild;
            currentNode.insertBefore(span, fChild);
            return traverse_and_insert(note, span, fChild, path, pos+1, endNode, endOffset);
        } else {
            currentNode = parentNode.removeChild(currentNode);
            span.appendChild(currentNode);

            var nextNode = nextSibling;
            if (nextSibling == null ) {
                while (parentNode.nextSibling == null) {
                    parentNode = parentNode.parentNode;
                }
                var span = get_new_span(note);
                nextNode = parentNode.nextSibling;
                parentNode.parentNode.insertBefore(span, nextNode);
            }
            return traverse_and_insert(note, span, nextNode, path, pos, endNode, endOffset);

        }
    }
    return false;
}

function get_select_topics(topic_objs) {
    var select_fields = '<select name="subtopic">';
    for (var i = 0; i < topic_objs.length; i++) {
        var obj   = topic_objs[i];
        var topic = $(obj).find('a').text();
        var input = $(obj).find('input');

        var topic_id = input.val();
        var checked  = input.attr('checked');

        var selected = '';
        if (checked == 'checked') {
            selected = ' selected="selected"';
        }
        if (!topic_id || isNaN(topic_id) || !topic) {
            continue;
        }
        select_fields += '<option value="' + topic_id + '"' + selected + '>' + topic + '</option>\n';
    }
    select_fields += '</select>';
    return select_fields;
}

function get_subtopics(option1) {
    var topic_objs = $(".research_topic");
    var objs       = $(".research_topic a");
    if (objs.length > 0) {
        var select_fields = '<table class="subtopic">\n';
        select_fields += '<tr><td><input type="radio" name="topic_type" value="1" checked/></td><td>' + option1 + '</td></tr>\n';
        select_fields += '<tr><td><input type="radio" name="topic_type" value="2"/></td>\n';
        select_fields += '<td><select name="subtopic_type"><option value="1" selected="selected">Sub-topic</option><option value="2">Super-topic</option></select> of '
        select_fields += get_select_topics(topic_objs) ;
        select_fields += '</td></tr></table>';
        return select_fields;
    }
    return '';
}

function get_select_value(objs) {
   if (objs.length >0 ){
       return objs[0].value;
   } else {
       return '0';
   }

}
function topic_post_data(obj) {
    var topic         = obj.children("input[name='topic']")[0].value;
    var subtopic      = obj.find("select[name='subtopic'] option:selected");
    var topic_type    = obj.find("input[name='topic_type']:checked");
    var subtopic_type = obj.find("select[name='subtopic_type'] option:selected");
    var postdata = {'topic' : topic, 
                    'subtopic'  :    get_select_value(subtopic), 
                    'topic_type':    get_select_value(topic_type), 
                    'subtopic_type': get_select_value(subtopic_type)};
    return postdata;                    
}                    

function startNewTopic() {
    var newDiv = $("<div></div>"); 
    newDiv.html('<div>Case name/Topic name</div><input type="text" name="topic"/>' + get_subtopics('Independent topic') );
    params = {
        title: "New Legal Research",  width: 450, closeText: "", 
        buttons: [{
            text: "Create", 
            click: function(e) {
                var postdata =  topic_post_data($(this));                
                $(e.target).css({opacity: 0.25}).unbind();

                $.ajax({type:"post", 
                        url: "/research/newtopic/", 
                        data: postdata})
                 .done(function () {
                     $(newDiv).dialog("close");
                     fetchLatestTopics();
                 })
                 .fail(function () {
                     newDiv.html("Sorry an error occurred. Try after sometime.");
                 });
            }
        }]
    };
    modify_dialog_params(params);
    $(newDiv).dialog(params);
    return false;

}

function get_topic(target) {
    var topic     = target.parent().parent().parent().children('.topic_title').text();
    if (topic.length <= 0) {
        var t = target.parent().parent();
        topic    = target.parent().parent().find('.topic_title_small').text();
    }

    return topic;
}

function share_topic(e) {
    var target   = $(e.target);
    var topic_id = target.attr('id').split('_')[1];
    var topic    = get_topic(target);

    var topic_privacy = target.attr('data-topicprivacy');
    var user_privacy  = target.attr('data-userprivacy');

    var user_privacy_text = privacy_choices[user_privacy];
    var topic_privacy_text = null;
    if (topic_privacy != 'None') {
        topic_privacy_text = privacy_choices[topic_privacy];
    }

    var newDiv = $("<div></div>");
    var priv_html = '';
    if (topic_privacy_text == null) {
        priv_html += '<p>The topic is shared with the default user privacy setting of <b>&quot;' + user_privacy_text + '&quot;</b>.</p>';
    } else {
        priv_html += '<p>The topic is shared with a custom privacy setting of <b>&quot;' + topic_privacy_text + '&quot;</b>.</p>';
    }
    
    priv_html += '<p> Change it below:</p> <table class="topic_privacy">'
    if (topic_privacy_text != null) {
        priv_html += '<tr><td><input type="radio" name="privacy" value="-1"/></td><td>Restore to default user privacy settings</td></tr>';
    }

    for (i = 0; i < privacy_order.length; i++){
        var row = '<tr><td><input type="radio" name="privacy" value="' +
                     privacy_order[i] + '"';
        if (topic_privacy == privacy_order[i]) {
            row += ' checked';
        }
        row += '/></td>\n<td>' + privacy_choices[privacy_order[i]] + '</td></tr>';
        priv_html += row;
    }

    priv_html += '</table>';
    newDiv.html(priv_html);
    var chprivacy = {
        text: "Change Privacy",
        icons: {secondary: 'ui-icon-arrowrefresh-1-e'},
        click: function(e) {
            var obj    = $(this);
            var inputs = obj.find("input[name='privacy']:checked");
            if (inputs.length <= 0) {
                newDiv.html('No privacy option selected');
                return;
            }
            var privacy = inputs[0].value;
            var postdata = {'privacy': privacy, 'topic_id': topic_id};
            $.ajax({type:"post", 
                    url: "/research/setprivacy/",
                    data: postdata})
             .done(function () {
                 target.attr('data-topicprivacy', privacy)
                 $(newDiv).dialog("close");
             })
             .fail(function () {
                 newDiv.html('Sorry an error happened. Please try after sometime');
             });

        }
    };

    var params = {title: "Privacy setting - " + topic,  closeText: "", 
                  width :450, buttons: [chprivacy]};
    modify_dialog_params(params);
    newDiv.dialog(params);

}
privacy_choices = {
    '0': 'Only me', 
    '2': 'Collaborators can only read my research', 
    '6': 'Collaborators can read and modify my research',
    '1': 'Anyone can read my research but no one can modify',
    '7': 'Anyone can read my research and collaborators can modify it'
};

privacy_order = ['0', '2', '6', '1', '7'];

function modtopic(e) {
    var target   = $(e.target);
    var topic_id = target.attr('id').split('_')[1];
    var topic    = target.attr('data-topic');

    var buttons = [];
    var newDiv = $("<div></div>"); 
    newDiv.html('<div>Topic</div><input type="text" name="topic" value="'+ topic + '"/>' + get_subtopics('As it is'));

    var del_button =  {
        text: "Delete It!",
        icons: {secondary: 'ui-icon-closethick'}, 
        click: function(e) {
            $(newDiv).dialog("close");
            deltopic_box(topic, topic_id);
        }
    }

    buttons.push(del_button);

    var update_button = {
        text: "Update",
        icons: {secondary: 'ui-icon-arrowrefresh-1-e'}, 
        click: function(e) {
            var postdata =  topic_post_data($(this));          
            $(e.target).css({opacity: 0.25}).unbind();

            $.ajax({type:"post", 
                    url: "/research/updatetopic/" + topic_id + "/", 
                    data: postdata})
             .done(function () {
                 $(newDiv).dialog("close");
                 location.reload();})
            .fail(function () {
                 newDiv.html("Sorry, got an error in updating the topic. Try after sometime.");
            });
        }
    };

    buttons.push(update_button);

    var topic_objs = $(".research_topic");

    var params = {title: "Modify Topic",  closeText: "", width :450, 
                  buttons: buttons};
    modify_dialog_params(params);
    $(newDiv).dialog(params);
}

function add_id(e) {
    var target = $(e.target);
    var topic_id = target.attr('id').split('_')[1];
    $.ajax({type:"post",
            url: "/research/addtopic/",
            data: {topic_id: topic_id}})
     .done(function () {
         fetchLatestTopics();
         target.html('Remove from dashboard');
         target.unbind();
         target.bind('click', remove_id);
     });

}

function remove_id(e) {
    var target = $(e.target);
    var topic_id = target.attr('id').split('_')[1];
    $.ajax({type:"post",
            url: "/research/rmtopic/",
            data: {topic_id: topic_id}})
     .done(function () {
         fetchLatestTopics();
         target.html('Add to dashboard');
         target.unbind();
         target.bind('click', add_id);
     });

}

function rmtopic(e) {
    var curr_topic = get_current_topic();
    var topic_id = curr_topic.topic_id;

    if (topic_id == "-1") {
        return;
    }

    $.ajax({type:"post",
            url: "/research/rmtopic/",
            data: {topic_id: topic_id} })
     .done(function () {
         fetchLatestTopics();
     });
}

function chtopic(event){
    var curr_topic = get_current_topic();

    $.ajax({type:"post",
            url: "/research/chtopic/",
            data: {'topic_id': curr_topic.topic_id} })
     .done(function () {
         fetchLatestTopics();
     });
    event.stopPropagation();
    event.preventDefault();
}

function uniq_name(e) {
    var obj = $('#uniq_button');
    if (obj.length <= 0) {
        create_uniq_name_button();
    }
    var text =  $('#id_uniqname').val();
    check_uniq_name(text);

}
function check_uniq_name(text) {
    var obj = $('#uniq_button');

    $.ajax({type:"get", 
                url: '/members/uniqname/',
                data: {'name': text}})
     .done(function (data, textStatus, jqXHR) {
         if (data == '1') {
             obj.button('option', 'label', 'Available');
             obj.button('option', 'icons', {primary: 'ui-icon-check'});
         } else if (data == '2') {
             obj.button('option', 'label', 'Invalid characters');
             obj.button('option', 'icons', {primary: 'ui-icon-close'});

         } else {
             obj.button('option', 'label', 'Not Available');
             obj.button('option', 'icons', {primary: 'ui-icon-close'});
         }
     });
}

function create_uniq_name_button() {
    var obj = $('<span id="uniq_button"></span');
    obj.insertAfter('#id_uniqname');   
    obj.button();
}

function copy_email(e) {
    var text = $(e.target).val();
    var uniq_name = text.substring(0, text.indexOf('@'));
    if (uniq_name) {
        $('#id_uniqname').attr('value', uniq_name);
        if (text.indexOf('@') > 0 && $('#uniq_button').length <= 0) {
            create_uniq_name_button();
            check_uniq_name(uniq_name); 
        }
    }
}

function send_fr_request(e) {
    var target   = $(e.target);
    target.css({opacity: 0.25}).unbind();
    var obj = target.parent();
    var email_id = obj.attr('id').split('_')[1];

    postdata = {'email_id': email_id};
    $.ajax({type:"post", 
            url: "/research/collab_request/",
            data: postdata})
    .done(function (data, textStatus, jqXHR) {
        if (data == '1') {
            obj.attr('id', '#frsent_'+email_id);
            obj.button().off('click');
            obj.button('option', 'label', 'Request sent for collboration');
            obj.button('option', 'icons', { primary: "ui-icon-arrowthick-1-ne"});
        }
     });
}

function accept_fr_request(e) {
    var target   = $(e.target);
    target.css({opacity: 0.25}).unbind();
    var obj = target.parent();
    var email_id = obj.attr('id').split('_')[1];

    postdata = {'email_id': email_id};
    $.ajax({type:"post", 
            url: "/research/accept_request/",
            data: postdata})
    .done(function (data, textStatus, jqXHR) {
        if (data == '1') {
            obj.attr('id', '#fr_'+email_id);
            obj.button().off('click');
            obj.button('destroy');
            obj.button({
                icons: { primary: "ui-icon-check" },
                label: 'Collaborator'
            }).click(remove_collaborator);
        }
     });

}

function remove_collaborator(e) {
    var target   = $(e.target);
    var obj      = target.parent();

    var email_id = obj.attr('id').split('_')[1];
    var name     = obj.attr('data-profilename');

    var newDiv = $('<div></div>');

    newDiv.html("Do you want to remove <b>" + name + '</b> as a collaborator?');

    var no_button = {
        text: "No",
        icons: {secondary: 'ui-icon-close'}, 
        click: function(e) {
            $(newDiv).dialog("close");
        }

    };

    var yes_button = {
        text: "Yes", 
        icons: {secondary: 'ui-icon-check'}, 
        click: function(e) {
            $.ajax({type: 'post', 
                    url: "/research/remove_collaborator/",
                    data: {'email_id': email_id}
            }).done( function () {
                $(newDiv).dialog('close');
                obj.attr('id', '#emailid_'+email_id);
                obj.button().off('click');
                obj.button('destroy');
                obj.button({
                    icons: { primary: "ui-icon-plusthick" },
                    label: 'Add as collaborator', 
                }).click(send_fr_request);
            }).fail(function () {
                 newDiv.html('Sorry an error happened. Please try after sometime');
            });
           
        }
    };

    var params = {title: "Remove collaborator?",  closeText: "", width :450, 
                  buttons: [no_button, yes_button]};
    modify_dialog_params(params);
    $(newDiv).dialog(params);


}
function friend_requests_button() {
    // self
    $('.self_person').button({
        icons: { primary: "ui-icon-home" },
        label: 'Self'
    });

    // send friend requests
    $('.send_fr').button({
        icons: { primary: "ui-icon-plusthick" },
        label: 'Add as collaborator', 
    }).click(send_fr_request);

    // friends
    $('.is_fr').button({
        icons: { primary: "ui-icon-check" },
        label: 'Collaborator'
    }).click(remove_collaborator);

    // respond to friend requests
    $('.fr_received').button({
        icons: { primary: "ui-icon-circle-plus" },
        label: 'Accept collaboration request'
    }).click(accept_fr_request);

    // friend requests in flight
    $('.fr_sent').button({
        icons: { primary: "ui-icon-arrowthick-1-ne" },
        label: 'Request sent for collboration'
    });

}
var idleTime = 0;
function inactivity_timer() {
    //Increment the idle time counter every minute.
    var idleInterval = setInterval(timerIncrement, 60000); // 1 minute

    //Zero the idle timer on mouse movement.
    $(this).mousemove(function (e) {
        idleTime = 0;
    });
    $(this).keypress(function (e) {
        idleTime = 0;
    });
}

function timerIncrement() {
    idleTime = idleTime + 1;
    if (idleTime > 10) { // 10 minutes
        $.ajax({type:"post",
                url: "/research/resettimer/"})
         .done(function () {
             idleTime = 0;
         });
    }
}

// jQuery plugin to prevent double submission of forms
jQuery.fn.preventDoubleSubmission = function() {
    $(this).on('submit',function(e){
        var $form = $(this);

        if ($form.data('submitted') === true) {
            // Previously submitted - don't submit again
            e.preventDefault();
        } else {
            // Mark it so that the next submit can be ignored
            $form.data('submitted', true);
        }
    });
 
    // Keep chainability
    return this;
};


function profile_pic_handler(e) {
    var newDiv  = $('<div></div>');
    var html_form = 'Please choose a new image file from your computer <input type="file" name="Choose file" accept="image/*"/>';
    newDiv.html(html_form);


    var params = {title: "Change profile picture",  closeText: "", width :450, 
                  buttons: [update_button]};
    modify_dialog_params(params);
    $(newDiv).dialog(params);
}

var xOffset = 10;
var yOffset = 30;
        
// these 2 variable determine popup's distance from the cursor
// you might want to adjust to get the right result
        
/* END CONFIG */
function img_preview(e) {
    this.t = this.title;
    this.title = "";    
    var c = (this.t != "") ? "<br/>" + this.t : "";
    var large_img = '<img src="'+ this.src +'" alt="Image preview" />';
    $("body").append("<p id='imgpreview'>"+ large_img + c +"</p>");             
    $("#imgpreview")
        .css("top",(e.pageY - xOffset) + "px")
        .css("left",(e.pageX + yOffset) + "px")
        .fadeIn("fast");                        
}

function img_preview_out(e){
    this.title = this.t;    
    $("#imgpreview").remove();
}
function img_preview_mv(e){
    $("#imgpreview")
        .css("top",(e.pageY - xOffset) + "px")
        .css("left",(e.pageX + yOffset) + "px");
}

function getSelectionAdv(e) {
    var buttons = [];
    var newDiv  = $("<div></div>"); 
    newDiv.html('<div class="advtext"><p>You can now select any section of a document to create annotations and comments. These can be added to your personalised research topic. You can also combine your notes to create a case brief, research paper, legal opinion etc.</p><p> This value add service is free for you to try for three months after which you may choose to opt for a premium membership or continue to avail our free services.</p></div>');


    var no_button = {
        text: "No, but remind me in a week!",
        icons: {secondary: 'ui-icon-closethick'}, 
        click: function(e) {
            $(e.target).css({opacity: 0.25}).unbind();

            $.ajax({type:"post", 
                    url: "/members/nonresearch/"}) 
             .done(function () {
                 $(newDiv).dialog("close");
                 location.reload();})
            .fail(function () {
                 newDiv.html("Sorry, got an error.");
            });
        }
    };

    buttons.push(no_button);
    var yes_button =  {
        text: "Yes, tell me more!",
        icons: {secondary: 'ui-icon-check'}, 
        click: function(e) {
            $(newDiv).dialog("close");
            window.open('https://indiankanoon.org/members/', "_blank");
        }
    }

    buttons.push(yes_button);

    var params = {title: "Legal Research Tool",  closeText: "", width :450, 
                  buttons: buttons, 
                  open: function(event, ui) {
                            $(":button:contains('Yes')").focus();
                        } 
                  };
    modify_dialog_params(params);
    $(newDiv).dialog(params);
}

function enableResearchDialog(e) {
    var buttons = [];
    var newDiv  = $("<div></div>"); 
    newDiv.html('<div class="advtext"><p>You are currently in a non research mode and cannot take research notes by selecting the text. Select a topic from the research dashboard and then a dialog for taking note will appear when you select text.</p><p>Would you like to change topic in the research dashboard?</p> </div>');


    var no_button = {
        text: "No, but remind me in a week!",
        icons: {secondary: 'ui-icon-closethick'}, 
        click: function(e) {
            $(e.target).css({opacity: 0.25}).unbind();

            $.ajax({type:"post", 
                    url: "/members/nonresearch/"}) 
             .done(function () {
                 $(newDiv).dialog("close");
                 location.reload();})
            .fail(function () {
                 newDiv.html("Sorry, got an error.");
            });
        }
    };

    buttons.push(no_button);
    var yes_button =  {
        text: "Yes!",
        icons: {secondary: 'ui-icon-check'}, 
        click: function(e) {
            $(newDiv).dialog("close");
            document.getElementById('research_search').scrollIntoView(); 
        }
    }

    buttons.push(yes_button);

    var params = {title: "Legal Research Tool",  closeText: "", width :450, 
                  buttons: buttons, 
                  open: function(event, ui) {
                            $(":button:contains('Yes')").focus();
                        } 
                  };
    modify_dialog_params(params);
    $(newDiv).dialog(params);
}

function registerEmailAlert(e) {
    if (e.data.is_auth == 'False') {
        return showSignUp(); 
    }

    if (e.data.valid_ag == 'False') {
        return showAgreementValidity();
    }

    if (e.data.is_valid == 'False') {
        return showRecharge();
    }

    var query    = $(e.target).parent().attr('data-query');

    var newDiv  = $("<div></div>");

    var agreement_text = '';
    if (e.data.is_agreement == 'True') {
        agreement_text = '<div class="inptc"><label><input type="checkbox" name="agreement" value="yes" style="width:20px;"/>I agree with the updated <a href="/members/agreement/" target="_blank">Terms and Conditions</a></label></div>';
    } 

    var html_text = '<div class="advtext"><p>You will get daily alerts for judgments matching the query <b>' + escapeHtml(query) + '</b>.</p> <p>The relevance level for query to document match will be at <div><select name="ranklaw"><option value="1">1 - Any match</option><option value="2">2 - Somewhat relevant</option> <option value="3" selected="selected">3 - Relevant (<i>recommended</i>)</option> <option value="4">4 - Very good match</option><option value="5">5 - Extremely relevant</option> </select></div>' + agreement_text + ' </div>';
    newDiv.html(html_text);

    var yes_button = {
        text: "Set up!",
        icons: {secondary: 'ui-icon-plusthick'}, 
        click: function(e) {
            var objs     = $(this).find("select[name='ranklaw'] option:selected");
            var ranklaw  =  get_select_value(objs);
            var agreement = $(this).find('input[name="agreement"]');

            if (agreement.length > 0 && !agreement[0].checked) {
                var new_html = html_text + '<div class="err">* Check the box above to agree with the terms and conditions</div>'
                newDiv.html(new_html);
                return;
            }
            var agree = 'notagree';
            if (agreement.length > 0 && agreement[0].checked) {
                agree = 'agree';
            }

            var data = {'query': query, 'ranklaw': ranklaw, 'agree': agree};
            $.ajax({type:"post", 
                    url: "/research/add_qwatch/",
                    data: data})
            .done(function (data, textStatus, jqXHR) {
                $(newDiv).dialog('option', 'buttons', {});
                newDiv.html('Query <b>' +  escapeHtml(query) + '</b> is successfully set up for alerts.' + jqXHR.responseText);
            })
            .fail(function ( jqXHR, textStatus, errorThrown )  {
                $(newDiv).dialog('option', 'buttons', {});
                newDiv.html("Sorry an error occurred. " + jqXHR.responseText);
            });

        }
    };

    var cancel_button = {
        text: "Cancel",
        icons: {secondary: 'ui-icon-closethick'}, 
        click: function(e) {
            $(newDiv).dialog("close");
        }
    };

    var buttons = [];
    buttons.push(cancel_button);
    buttons.push(yes_button);
   
    var params = {title: "Register for email alert",  closeText: "", 
                  width :450, buttons: buttons};

    modify_dialog_params(params);
    $(newDiv).dialog(params);


}

function showSignUp() {
    var params = {title: "Login",  closeText: "", width :450};
    var newDiv  = $("<div></div>"); 
    newDiv.html('<div class="advtext">You are currently not logged in to set up the alerts. Login as Premium Member <a href="/members/login/">here</a></div>');
    modify_dialog_params(params);
    $(newDiv).dialog(params);

}

function showAgreementValidity() {
    var params = {title: "Terms & Conditions", width :450};
    var newDiv  = $("<div></div>"); 
    newDiv.html('<div class="advtext">Your have not yet agreed with our Terms and Conditions. Accept it <a href="/members/agreement/?reagree=True">here</a> to proceed.</div>');
    modify_dialog_params(params);
    $(newDiv).dialog(params);

}
function showRecharge() {
    var params = {title: "Account not valid",  closeText: "", width :450};
    var newDiv  = $("<div></div>"); 
    newDiv.html('<div class="advtext">Your account is no longer valid. Recharge <a href="/members/payoptions/">here</a> to continue setting up alerts</div>');
    modify_dialog_params(params);
    $(newDiv).dialog(params);

}

function newDialog(title, htmltext) {
    var params = {title: title,  closeText: "", width :450};
    var newDiv  = $("<div></div>"); 
    newDiv.html(htmltext);
    modify_dialog_params(params);
    $(newDiv).dialog(params);
}

function chranklaw(e) {
    var obj = $(e.target);
    var queryid = obj.attr('data-queryid');
    var query   = obj.attr('data-query');
    var option  = obj.parent().find("select[name='ranklaw'] option:selected");

    var ranklaw = option.attr('value');
    var ranklaw_text = option.text()

    var postdata = {'ranklaw': ranklaw, 'qid': queryid};

    $.ajax({type: 'post',
            url: '/research/update_qwatch/',
            data: postdata})
    .done(function (data, textStatus, jqXHR) {
        newDialog('Success', 'Successfully changed the relevance level for the query <b>' + query + '</b> to <b>'+ranklaw_text +'</b>');

    })
    .fail(function (jqXHR, textStatus, errorThrown) {
        newDialog('Error', 'Sorry an error occured while changing the relevance level for query <b>' + query + '</b>. Please try after sometime');
    });
}

function querydel(e) {
    var obj = $(e.target);
    var queryid = obj.attr('data-queryid');
    var query   = obj.attr('data-query');

    var newDiv  = $("<div></div>"); 
    newDiv.html('Do you want to delete the query <b>' + escapeHtml(query) + '</b>? It means you will no longer be getting alerts for this query.');

    var yes_button = {
        text: "Yes, delete it!",
        icons: {secondary: 'ui-icon-check'},
        click: function(e) {
            var data = {'qid': queryid};
            $.ajax({type:"post", 
                    url: "/research/del_qwatch/",
                    data: data})
            .done(function (data, textStatus, jqXHR) {
                location.reload();
            })
            .fail(function ( jqXHR, textStatus, errorThrown )  {
                newDiv.html("Sorry an error occurred. Try after sometime.");
            });

        }
    };
    var no_button = {
        text: "No",
        icons: {secondary: 'ui-icon-closethick'}, 
        click: function(e) {
            $(newDiv).dialog("close");
        }
    };

    var buttons = [];
    buttons.push(no_button);
    buttons.push(yes_button);


    var params = {title: 'Delete query',  closeText: "", width :450, 
                  buttons:  buttons};
    modify_dialog_params(params);
    $(newDiv).dialog(params);

}


