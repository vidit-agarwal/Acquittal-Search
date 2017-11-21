<?php

	$mysqli = NEW  MySQLi('tblproduction.cmx4mndnhogx.ap-south-1.rds.amazonaws.com', 'root', 'Aniket2606' , 'machineLearning') ;
     
    
     
     $query = $mysqli->query("SELECT * FROM lawyer_data  ; ");

     

     

?>
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>All Lawyers</title>
	<link rel="icon" href="images/logo.png">	
	 <!--<link rel="stylesheet" href="table_ui/css/footable.bootstrap.css">
	 <link rel="stylesheet" href="table_ui/css/footable.bootstrap.min.css">-->

	<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
	
	<!--<script type="text/javascript" src="table_ui/js/footable.js"></script>
    <script type="text/javascript" src="table_ui/js/footable.min.js"></script>-->
      <link rel="stylesheet" href="	css/style.css">

      
</head>
<body>
	
<div style="overflow-x:auto;">
	<table class="lawyer_table" data-paging="true" border=" 1px solid black " border-collapse="collapse " style="width:100% ;">
		<thead>
				<tr>
					<th>Sno </th>
					<th>URL</th>
					<th>Name</th>
					
						

				</tr>
		</thead>
		<tbody>
			<?php
				while($row = mysqli_fetch_row($query))
			     {
			     	echo "<tr>";
			     	echo "<td>".$row[0]."</td>" ;
			     	echo '<td> <a href='.$row[1].'>'.$row[1].'</a> </td>' ;
			     	echo "<td>".$row[2]."</td>" ;
			     	
			     	
			  
			     	echo "</tr>" ;
			     }


			?>
		</tbody>

	</table>

</div>

</body>
</html>