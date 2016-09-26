<h1>Count Word API</h1>
<h3>Features</h3>
<ul>
    <li>Pass a site and a word to recive a JSON with how many this word have in the page.</li>
    <li>List all countes.</li>
</ul>
<h3>Usage:</h3>
<h4>Get all counters</h4>
Get this page to see all counters <a href="counters">List counters</a>
<h4>Make a count in a Web Site</h4>
Make a POST request to url /counters/get with two args:
<ul>
    <li>web_page='http://example.com/'</li>
    <li>word='example'</li>
</ul>
You can use <a href="https://github.com/jkbrzt/httpie">httpie</a> to make the POST
request.
Example:
<br />
<br />
http --form POST http://localhost:8000/counters/get web_page='http://example.com/' word='example'
