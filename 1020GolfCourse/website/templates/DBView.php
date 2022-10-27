{% extends "base.html" %} {% block title } DataBase {% endblock %} {% block content %}
<head>
    <title> Database </title>

</head>
<body>
    <table>
        <tr>
            <th> </th>
            <th> </th>
            <th> </th>
            <th> </th>
            <th> </th>
            <th> </th>
            <th> </th>
            <th> </th>
            <th> </th>
            <th> </th>
        </tr>
        <?php
        $conn = SQLALCHEMY("localhost", "root", "GOLFCOURSEPROJECT", "golfreview")
        if ($conn-> connect_error) {
            die("Connection failed:". $conn-> connect_error);
        }
        $sql = "SELECT date, gender, golf_Course, golf_Rating, visit, golf_ball, club, review_Rate, add_Feedback from golfreview.db";
        $result = $conn-> query($sql);

        if ($result-> num_rows >0){
            while($row = $result-> fetch_assoc()){
                echo "<tr><td>". $row["date"] ."</td><td>". $row["gender"] ."</td><td>". $row["golf_Course"] ."</td><td>". $row["golf_Rating"] 
                ."</td><td>". $row["visit"] ."</td><td>". $row["golf_ball"] ."</td><td>". $row["club"] ."</td><td>". $row["review_Rate"] 
                ."</td><td>". $row["add_Feedback"] ."</td></tr>";
            }
            echo "</table>";
        }
        else{
            echo "0 result";
        }
        $conn-> close();

        ?>
    </table>    
</body>
{% endblock %}