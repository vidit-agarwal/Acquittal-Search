$(document).ready( 
  function () {
      $('table').addClass('hidden');
      $('.catcheckall').addClass('hidden');

      function get_tables(basename) {
          var tableId = basename + '-table';
          return  $('table').filter(
                    function () {
                      return this.id == tableId;
                    }
                  )
      }

      $(".catselectall").click(
        function() {
            var tables  = get_tables(this.value); 
            var inputboxes  = tables.find('input');
            var catcheckall = '#' + this.value;
            var checked = this.checked;
 
            if (checked == true) {
                tables.addClass('hidden');
                $(catcheckall).addClass('hidden');
                inputboxes.attr('checked', true);
            } else {
                tables.removeClass('hidden');
                $(catcheckall).removeClass('hidden');
                inputboxes.attr('checked', false);
            }
        }
      )

      $('.catcheckall').click(
        function() {
          var tables = get_tables(this.id);
          var inputboxes = tables.find('input');
          if (this.value == 'Check All') {
              this.value = 'Uncheck All';
              inputboxes.attr('checked', true);
          } else {
              this.value = 'Check All';
              inputboxes.attr('checked', false);
          }
        }
      )
  }
)

