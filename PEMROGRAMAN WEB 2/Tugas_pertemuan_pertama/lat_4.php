<html>
    <head>
        <title>Contoh Skrip PHP</title>
    </head>
    <body>
        <?
            $nilai = 85;
            $nama = "Amir";
            if ($nilai >= 80){
                echo "$nama mendapat nilai A";
            } elseif ($nilai >= 70){
                echo "$nama mendapat nilai B";
            } elseif ($nilai >= 60){
                echo "$nama mendapat nilai C";
            } elseif ($nilai >= 50){
                echo "$nama mendapat nilai D";
            } else {
                echo "$nama mendapat nilai E";
            }
        ?>
    </body>
</html>