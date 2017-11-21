<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<!-- saved from url=(0038)https://indiankanoon.org/advanced.html -->
<html >
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

   <link rel="icon" href="images/logo.png">   

    <link type="text/css" href="search/jquery-ui.min.css" rel="stylesheet">
    <link type="text/css" href="search/jquery-ui.theme.min.css" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="search/search_desktop_v14.css">



    <title>Advanced Search- Acquittal Search</title>


</head>

<body data-gr-c-s-loaded="true" style="background-color: rgb(255, 255, 255); width: 740px;" cz-shortcut-listen="true">



    <div class="top_bar">
        <div class="small_logo">
         <img src="images/logo.png" alt="eror" style="margin-right:5px;"><b style="float:right ; margin-top: -20px; font-size: 17px; margin-left: 8px; display: inline">Acquittal Search</b>
        </div>
        <div class="static_bar">

    Advanced Search


            <div class="right_links">

    <a class="top_links" href="index.php">Main Search</a>   |
    <a class="top_links" href="about/about.php">About</a>

            </div>
        </div>
    </div>

    <div class="info_indian_kanoon">





<div style="width: 700px;">

  <form name="advform" method="GET" action="   " style="font-family: arial;">
  <div style="float:right;padding: 10px;font-size: 1.2em;font-weight: bold;">
    <input type="submit" value="Search&gt;&gt;">
  </div>

  <div style="width: 600px;">
    <div class="field_adv_search">
      <span class="adv_field_desc">Document or Title or Citation</span>
      <span class="adv_field_option"><input size="30" type="text" name="main"></span>
    </div>

    <div class="field_adv_search">
      <span class="adv_field_desc">Only Title</span>
      <span class="adv_field_option"><input size="30" type="text" name="title"></span>
    </div>

    <div class="field_adv_search">
      <span class="adv_field_desc">Only Citation Number</span>
      <span class="adv_field_option"><input size="30" type="text" name="citations"></span>
    </div>

    <div class="field_adv_search">
      <span class="adv_field_desc">Judge</span>
      <span class="adv_field_option"><input size="30" type="text" name="author"></span>
    </div>

    <div class="field_adv_search">
      <span class="adv_field_desc">Order results by </span>
      <span class="adv_field_option">
        <input type="RADIO" name="sortby" value="relevance" checked="">Relevance
        <input type="RADIO" name="sortby" value="mostrecent"> Most Recent
        <input type="RADIO" name="sortby" value="leastrecent"> Least Recent
      </span>
    </div>

    <div class="field_adv_search">
      <div class="adv_field_desc">Date</div>
      <div class="adv_field_option">
         <input id="anchor1" type="text" name="fromdate" style="width:100px;" value="DD-MM-YYYY" class="hasDatepicker"><button type="button" class="ui-datepicker-trigger">Calendar</button>
         <input id="anchor2" type="text" name="todate" style="width:100px;" value="DD-MM-YYYY" class="hasDatepicker"><button type="button" class="ui-datepicker-trigger">Calendar</button>
      </div>
    </div>


    <div class="field_adv_search" id="legal-doctypes">
      <div class="adv_field_desc">Types of legal documents</div>
      <div class="adv_field_option">
      </div>
    </div>

      <div class="adv_doctypes"> Acts
        <div class="adv_field_option">
          <input class="catselectall" type="checkbox" name="doctypes" value="laws" checked="">
          <input class="catcheckall hidden" id="laws" type="button" name="CheckAll" value="Check All">
        </div>
      </div>
      <table class="doctypes hidden" id="laws-table">

          <tbody><tr>

              <td>
                <input type="checkbox" name="doctypes" value="act"> Complete Act
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="section"> Section
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="subsection"> Subsection
              </td>

          </tr>

          <tr>

              <td>
                <input type="checkbox" name="doctypes" value="subsubsection"> Subsubsection
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="subsubsubsection"> Sub-3-section
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="subsubsubsubsection"> Sub-4-section
              </td>

          </tr>

          <tr>

              <td>
                <input type="checkbox" name="doctypes" value="subsubsubsubsubsection"> Sub-5-section
              </td>

          </tr>

      </tbody></table>

      <div class="adv_doctypes"> Court Judgments
        <div class="adv_field_option">
          <input class="catselectall" type="checkbox" name="doctypes" value="judgments" checked="">
          <input class="catcheckall hidden" id="judgments" type="button" name="CheckAll" value="Check All">
        </div>
      </div>
      <table class="doctypes hidden" id="judgments-table">

          <tbody><tr>

              <td>
                <input type="checkbox" name="doctypes" value="supremecourt"> Supremecourt
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="scorders"> SC - Daily Orders
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="allahabad"> Allahabad
              </td>

          </tr>

          <tr>

              <td>
                <input type="checkbox" name="doctypes" value="andhra"> Andhra
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="bombay"> Bombay
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="chattisgarh"> Chattisgarh
              </td>

          </tr>

          <tr>

              <td>
                <input type="checkbox" name="doctypes" value="chennai"> Madras
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="delhi"> Delhi
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="gauhati"> Gauhati
              </td>

          </tr>

          <tr>

              <td>
                <input type="checkbox" name="doctypes" value="gujarat"> Gujarat
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="himachal_pradesh"> Himachal Pradesh
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="jammu"> Jammu
              </td>

          </tr>

          <tr>

              <td>
                <input type="checkbox" name="doctypes" value="jharkhand"> Jharkhand
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="karnataka"> Karnataka
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="kerala"> Kerala
              </td>

          </tr>

          <tr>

              <td>
                <input type="checkbox" name="doctypes" value="kolkata"> Kolkata
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="lucknow"> Lucknow
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="madhyapradesh"> Madhya Pradesh
              </td>

          </tr>

          <tr>

              <td>
                <input type="checkbox" name="doctypes" value="orissa"> Orissa
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="patna"> Patna
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="punjab"> Punjab-Haryana
              </td>

          </tr>

          <tr>

              <td>
                <input type="checkbox" name="doctypes" value="rajasthan"> Rajasthan
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="sikkim"> Sikkim
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="uttaranchal"> Uttaranchal
              </td>

          </tr>

          <tr>

              <td>
                <input type="checkbox" name="doctypes" value="kolkata_app"> Kolakata Appellete
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="jodhpur"> Jodhpur
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="patna_orders"> Patna-Orders
              </td>

          </tr>

          <tr>

              <td>
                <input type="checkbox" name="doctypes" value="srinagar"> Srinagar
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="meghalaya"> Meghalaya
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="delhidc"> Delhi District Ct
              </td>

          </tr>



      </tbody></table>

      <div class="adv_doctypes"> Tribunals
        <div class="adv_field_option">
          <input class="catselectall" type="checkbox" name="doctypes" value="tribunals" checked="">
          <input class="catcheckall hidden" id="tribunals" type="button" name="CheckAll" value="Check All">
        </div>
      </div>
      <table class="doctypes hidden" id="tribunals-table">

          <tbody><tr>

              <td>
                <input type="checkbox" name="doctypes" value="aptel"> Aptel
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="authority"> Authority
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="cat"> CAT
              </td>

          </tr>

          <tr>

              <td>
                <input type="checkbox" name="doctypes" value="cegat"> Cegat
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="cerc"> CERC
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="cic"> CIC
              </td>

          </tr>

          <tr>

              <td>
                <input type="checkbox" name="doctypes" value="clb"> CLB
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="consumer"> Consumer Courts
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="copyrightboard"> Copyright Board
              </td>

          </tr>

          <tr>

              <td>
                <input type="checkbox" name="doctypes" value="drat"> Debt Recovery
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="greentribunal"> Green Tribunal
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="cci"> Competition Commission
              </td>

          </tr>

          <tr>

              <td>
                <input type="checkbox" name="doctypes" value="ipab"> IPAB
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="itat"> ITAT
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="mrtp"> Monopoly
              </td>

          </tr>

          <tr>

              <td>
                <input type="checkbox" name="doctypes" value="sebisat"> SAT
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="stt"> State Taxation
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="tdsat"> TDSAT
              </td>

          </tr>

          <tr>

              <td>
                <input type="checkbox" name="doctypes" value="trademark"> Trademark
              </td>

              <td>
                <input type="checkbox" name="doctypes" value="cestat"> Cestat
              </td>

          </tr>

      </tbody></table>

    <div>

</div>

    </div>
  </form>


    <script type="text/javascript" src="search/jquery-1.11.1.min.js"></script>
    <script type="text/javascript" src="search/jquery-ui.min.js"></script>



<script type="text/javascript">
$(document).ready(
  function () {
      $("#anchor1").datepicker({ showOn: "button", changeMonth: true, buttonText: "Calendar", changeYear: true, yearRange: "-65:", maxDate: "+0d", dateFormat:"dd-mm-yy" });
      $("#anchor2").datepicker({ showOn: "button", buttonText: "Calendar", changeMonth: true, changeYear: true, yearRange: "-65:", maxDate: "+0d", dateFormat:"dd-mm-yy" });
  }
);
</script>

<script type="text/javascript" src="search/adv_search.js"></script>

<script type="text/javascript">
$(document).ready(
  function () {
        $("body").css("background-color", "white");
        $("body").css("width", "740px");
  }
);
</script>







</div>
</div>
<div id="ui-datepicker-div" class="ui-datepicker ui-widget ui-widget-content ui-helper-clearfix ui-corner-all">

</div>
</body>
</html>
