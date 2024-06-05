<?php

$video = '<Header GuideClass="Video" Description="V&#xED;deo" VideoDate="2003-03-31&#x20;11&#x3A;19&#x3A;18.560"/>';
$img27978 = '<Header GuideClass="Image" Description="Imagem" ImageDate="2003-03-31&#x20;11&#x3A;19&#x3A;11.360"/>';
$img124509 = '<Header GuideClass="Image" Description="RECEITA" ImageDate="2018-04-19"/>';

if (strstr($img27978, 'Description="')) {
    $fileName = html_entity_decode(reset(explode('"', end(explode('Description="', $img27978)))));
    echo "\nentrou\n\n";
  }
  else {
    $fileName = '';
}

echo '$fileName: ' . $fileName;