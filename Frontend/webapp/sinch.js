function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false );
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

httpGet("https://api.particle.io/v1/devices/53ff6f065067544833490587/temp?access_token=bb3dc001dbd1e097caf31f118ab706f977085740")
