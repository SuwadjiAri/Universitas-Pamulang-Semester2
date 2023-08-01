<html>
    <head>
        <title>Contoh Skrip PHP</title>
    </head>
    <body>
        Tanggal Lahir:
        <select name="tanggal">
            <option value="0" selected>Tanggal</option>
            <?
                for ($i=1; $i<32; $i++){
                    echo "<option value=\"$i\">$i</option>\n";
                }
            ?>
        </select>
    </body>
</html>