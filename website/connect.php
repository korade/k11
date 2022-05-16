<?php  
$server_name="localhost";
$username="root";
$password="";
$database_name="test";
$conn=mysqli_connect($server_name,$username,$password,$database_name);
if(!$conn)
{
	die("Connection Failed:".mysqli_connect_error());
}
if(isset($_POST['submit']))
{
	$fname=$_POST['fname'];
	$lname=$_POST['lname'];
	$age=$_POST['age'];
	$email=$_POST['email'];
	$PhoneNo=$_POST['PhoneNo'];
	//$gender=$_POST['gender'];
	
	$sql_query="INSERT INTO registration(fname,lname,age,email,PhoneNo)VALUES('$fname','$lname','$age','$email','$PhoneNo')";

	if (mysqli_query($conn,$sql_query)) 
	{
		echo "Connected successfuly";
       
    }
    else
	{
		echo "Error: " .$sql. "" .mysqli_error($conn);
	}
	mysqli_close($conn);
}

?>






