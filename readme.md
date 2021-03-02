![Dweet Gallery](https://www.dwitter.net/static/img/logo_small.png)  
# Dweet Gallery: The Offline Dweet Viewer

I just got a new office, and I was thinking, "What inspires me most?  What conveys the beauty of code most aptly?"

"What would be really cheap to make, yet leverage a lot of other people's cleverness?"

The Dweet Gallery was born.
- Work in progress (of course)
- The default HTML file runs the top 1000 dweets by 'awesome count' on a 10 minute timer, then randomly selects another
- Suggestions for improvement / pull requests for actual improvement welcome
- Trivia: the popularity of dweets on [dwitter.net](https://www.dwitter.net/) follows a [power law](https://en.wikipedia.org/wiki/Power_law#/media/File:Long_tail.svg)

## Credit Where Credit is Due:
The fine people over at Dwitter.net made all the dweets.  Check out  [dwitter.net](https://www.dwitter.net/)

## The Dwitter API:
 GET www.dwitter.net/api/dweets/  - list of the last 10 dweets

       ?limit=100            - number of results to return, default 10, max 100 (subject to change)
       &offset=200           - offset page by 200 dweets
       &remix_of=123         - all remixes of 123
       &author=lionleaf      - dweets by author

### Calling the API:
 ```bash
 curl "https://www.dwitter.net/api/dweets/?limit=1"
 ```

#### Example of Return from API:
 {"count":17129,"next":"http://www.dwitter.net/api/dweets/?limit=1&offset=1","previous":null,"results":[{"id":21764,"code":"c.width=200\r\nt?0:(a=2**.5,b=0,p=2+a)\r\nA=a**.5\r\nat=A/2+.5/A\r\nbt=(1+b)*A/(a+b)\r\npt=(1+at)*p*bt/(1+bt)\r\na=at\r\nb=bt\r\np=pt\r\nx.fillText(p,5,10)","posted":"2021-02-25T16:17:29.254960Z","author":{"username":"Odog8","date_joined":"2019-09-27","link":"https://www.dwitter.net/u/Odog8","avatar":"https://gravatar.com/avatar/e2e5df4b52feaa72528a06bd24aa015c?d=retro"},"link":"https://www.dwitter.net/d/21764","awesome_count":1,"remix_of":21751}]}

## Built in functions for Dwitter

u(t) is called 60 times per second.
    t: Elapsed time in seconds.
    S: Shorthand for Math.sin.  
    C: Shorthand for Math.cos.
    T: Shorthand for Math.tan.
    R: Function that generates rgba-strings, usage ex.: R(255, 255, 255, 0.5)
    c: A 1920x1080 canvas.
    x: A 2D context for that canvas.

### boilerplate:
- this stuff is the same every time, and the pulled dweet goes after the 'for':

function u(t) {
for

}

### Blatantly copied and then modified from:	
["Tweet Demo"](https://arkt.is/t/)
- this works by converting the string to base64, then you throw that into the url after the t/


## Serving
python -m http.server
(or similar)


## The 'Engine'
c.width = 1920;
c.height = 1080;
S = Math.sin;
C = Math.cos;
T = Math.tan;
R = function(r,g,b,a) {
    a = a === undefined ? 1 : a;
    return "rgba("+(r|0)+","+(g|0)+","+(b|0)+","+a+")";
};
x = c.getContext("2d");
frame = 0;
function loop() {
    u(frame++ / 60);
    requestAnimationFrame(loop);
};
function u(t) {c.width|=0
for(i=2e3;i--;x.fillRect(700+i/4+S(i)*99,540+S(t)*400+C(i)*99,19,19))x.fillStyle=`hsl(${i&896},50%,${S(i-S(t))**6*255}%)`}
loop();
          

## Caveats
- You might have more luck with a bunch of gif recordings of the dweets, which is actually a feature of [dwitter.net](https://www.dwitter.net/)
  - However, GIF recording is very intensive on the site and actually caused my computer to crash in Firefox, and the feature doesn't really seem to work in Chrome either (for me).  So I went with this.

## bug fixes in the API pulls
- \r\n replace all with ;
- The rest of my little fixes to the API call results are in 'json_pull_fix.py
