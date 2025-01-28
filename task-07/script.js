var getweather_button=document.getElementById("getweather");
var myweather_button=document.getElementById("myweather");
var details=document.getElementById("details");
const apikey='74e5f5341fd43abcd051b787bdfbce5a';
details.style.display="none";

function fetchweather(url){
    var location=document.getElementById("location");
    var pic=document.getElementById("pic");
    var temperature=document.getElementById("temperature");
    var description=document.getElementById("description");
    var maxtemp=document.getElementById("maxtemp");
    var mintemp=document.getElementById("mintemp");
    var humidity=document.getElementById("humidity");
    fetch(url)
        .then(response=>response.json())
        .then(data=>{
            var name=data.name;
            var country=data.sys.country;
            var img=data.weather[0].icon;
            var t=data.main.temp;
            var max_temp=data.main.temp_max;
            var min_temp=data.main.temp_min;
            var hum=data.main.humidity;
            var des=data.weather[0]["main"];
            var iconurl=`https://openweathermap.org/img/wn/${img}@2x.png`;
            pic.src=iconurl;
            details.style.display="block";
            temperature.textContent=t+" \u00B0C";
            location.textContent=`${name}, ${country}`;
            maxtemp.textContent=`Maximum Temperature: ${max_temp} \u00B0C`;
            mintemp.textContent=`Minimum Temperature: ${min_temp} \u00B0C`;
            humidity.textContent=`Humidity: ${hum}%`;
            description.textContent=des;
        })
        .catch(()=>{
            details.style.display='block';
            location.textContent='Error! Please enter a valid city name.';
        });

}

myweather_button.onclick=function(){
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position){
            var lat=position.coords.latitude;
            var lon=position.coords.longitude;
            var link=`https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${apikey}&units=metric`;
            fetchweather(link);
        })}
    else{
        details.style.display='block';
        location.textContent='An error occured. Please try again';
    }
    
}

getweather_button.onclick=function(){
    var inputval=document.getElementById("inputcity").value;
    link=`https://api.openweathermap.org/data/2.5/weather?q=${inputval}&appid=${apikey}&units=metric`;
    fetchweather(link);


}
