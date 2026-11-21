---

title: "jday(1)"
name: "jday"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jday/"
description: "jday, j2d – astronomical julian date conversion utilities"
---

<h2>NAME</h2>
<p> jday, j2d &#8211; astronomical julian date conversion utilities</p>
<p> <code>jday</code></p>
<dl>
<dt><code>jday [-d [-]year-mm-dd hh:mm:ss]</code></dt>
<dd>
</dd><dt><code>jday [&#8211;version]</code></dt>
<dd>
</dd><dt><code>jday [&#8211;h[elp]]</code></dt>
<dd>
</dd><dt><code>j2d &lt;julian decimal date&gt;</code></dt>
<dd>
</dd><dt><code>j2d [&#8211;version]</code></dt>
<dd>
</dd><dt><code>j2d [&#8211;h[elp]]</code></dt>
<dd></dd></dl>
<p> <i>jday and j2d</i> are command line utilities to convert calendar dates to astronomical julian dates, and julian dates to calendar dates. There is a corresponding library <i>libjday.a</i> which can be used for the same functionality within applications.</p>
<h2>OPTIONS</h2>
<p> <i>jday</i> accepts the following options:</p>
<dl>
<dt><code>none at all</code></dt>
<dd> <i>jday</i> will simply print out the julian date based on the date and time found on the system.</dd>
<dt><code>[year [month [day [hour [minute [second]]]]]]</code></dt>
<dd> Always in that order, to override that value found on the system.</dd>
<dt><code>-d [-]year-mm-dd hh:mm:ss</code></dt>
<dd> Specify a year in the same format as that printed out by <i>j2d</i></dd>
<dt><i>j2d</i> accepts the following options:</dt>
<dd>
</dd><dt><code>&lt;julian decimal date&gt;</code></dt>
<dd> This is the only, and required argument to <i>j2d</i></dd>
<dt><i>both commands</i> accept the following options:</dt>
<dd>
</dd><dt><code>&#8211;version</code></dt>
<dd> Display the version of the programs.</dd>
<dt><code>&#8211;h[elp]</code></dt>
<dd> Display a command help message</dd></dl>
<h2>EXAMPLES</h2>
<p> <code>$ jday 1970 1 1 12 0 0</code><br />
 2440588.000000<br />
 $ jday 0 1 1 12 0 0<br />
 1721058.000000<br />
 $ jday -4712 1 1 12 0 0<br />
 0.000000<br />
 $ jday -d -4712-01-01 12:00:00<br />
 0.000000<br />
 $ j2d 0.0<br />
 -4712-01-01 12:00:00<br />
 $ j2d 1721058.0<br />
 0-01-01 12:00:00<br />
 $ j2d 2440588.0<br />
 1970-01-01 12:00:00</p>
<h2>SEE ALSO</h2>
<p> Time Standard: <a rel="nofollow" href="http://tycho.usno.navy.mil">http://tycho.usno.navy.mil</a><br />
 Systems of time: <a rel="nofollow" href="http://tycho.usno.navy.mil/systime.html">http://tycho.usno.navy.mil/systime.html</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1986-2005, Hiram Clawson</p>
<dl>
<dt>jday at hiram.ws</dt>
<dd>
</dd><dt>All rights reserved.</dt>
<dd>
</dd><dt>Redistribution and use in source and binary forms, with or</dt>
<dd> without modification, are permitted provided that the following conditions are met:</dd>
<dt>Redistributions of source code must retain the above</dt>
<dd> copyright notice, this list of conditions and the following disclaimer.</dd>
<dt>Redistributions in binary form must reproduce the</dt>
<dd> above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.</dd>
<dt>Neither name of The Museum of Hiram nor the names of</dt>
<dd> its contributors may be used to endorse or promote products derived from this software without specific prior written permission.</dd>
<dt>THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND</dt>
<dd> CONTRIBUTORS &#8220;AS IS&#8221; AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. </dd>
</dl>
