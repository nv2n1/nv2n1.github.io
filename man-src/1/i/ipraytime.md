---
title: "ipraytime(1)"
name: "ipraytime"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipraytime/"
description: "ipraytime – An Islamic Prayer Times Calculator"
---

<h2>NAME</h2>
<p> ipraytime &#8211; An Islamic Prayer Times Calculator</p>
<h2>SYNOPSIS</h2>
<p> <code>ipraytime</code> [<code>&#8211;date</code> yyyymmdd<i>]</i> [<code>&#8211;latitude</code> real_num<i>]</i> [<code>&#8211;longitude</code> real_num<i>]</i> [<code>&#8211;utcdiff</code> real_num<i>]</i> [<code>&#8211;method</code> int_num<i>]</i> [<code>&#8211;ishaangle</code> real_num<i>]</i> [<code>&#8211;fajrangle</code> real_num<i>]</i> [<code>&#8211;dst</code> int_num<i>]</i> [<code>&#8211;dst-start</code> yyyymmdd<i>]</i> [<code>&#8211;dst-end</code> yyyymmdd<i>]</i> [<code>&#8211;round</code> int_num<i>]</i> [<code>&#8211;extreme</code> int_num<i>]</i> [<code>&#8211;sea-level</code> int_num<i>]</i> [<code>&#8211;month</code> [int_num]<i>]</i> [<code>&#8211;year</code> [int_num]<i>]</i> [<code>&#8211;file</code> pref_file<i>]</i> [<code>&#8211;end</code>] [<code>&#8211;brief</code>] [<code>&#8211;help</code>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>ipraytime</code> program is a generator of Islamic prayer time schedules for any given location. <code>ipraytime</code> also calculates the appropriate Qibla direction (heading towards the Kabaa) based on the given location. <code>ipraytime</code> in its single day format is also capable of calculating Imsaak times (ie. the times when one is to start fasting). <code>ipraytime</code> is also capable of generating a schedule for an entire month or year based on command-line arguments. The program is also able to print the schedules for the rest of the current month so as to skip days that have already passed. <code>ipraytime</code> also has a minimalistic option to simply show a one liner of the prayer times in its single day format. </p>
<p> <code>ipraytime</code> has multiple ways of conveying info and settings to it. The order of precedence (from highest to lowest) is, the command-line followed by the environment variable setting (IPT_DATA) to the data being presented in <code>ipraytime</code>&#8216;s RC file (<i>~/.iprayrc</i>) in one&#8217;s home directory. If none of the above is found, <code>ipraytime</code> defaults to using Makkah&#8217;s location with the host machine&#8217;s current date settings.</p>
<h2>OPTIONS</h2>
<p> <code>ipraytime</code> follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of all options is noted below:</p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of options</p>
<dt><code>-d, &#8211;date </code><i>yyyymmdd</i></p>
<dd> Specify the Gregorian date to use where `y&#8217; stands for year, `m&#8217; for month and `d&#8217; for day</p>
<dt><code>-lat, &#8211;latitude </code><i>real_num</i></p>
<dd> Specify the latitude setting to use during calculations. The value could be any real number</p>
<dt><code>-lon, &#8211;longitude </code><i>real_num</i></p>
<dd> Specify the longitude setting to use during calculations. The value could be any real number</p>
<dt><code>-sea, &#8211;sea-level </code><i>real_num</i></p>
<dd> Specify height above Sea level (in meters)</p>
<dt><code>-u, &#8211;utcdiff </code><i>real_num</i></p>
<dd> Specify the difference between the specified timezone and that of GMT/UTC. The value could be any real number</p>
<dt><code>-a, &#8211;anglemethod </code><i>[int_num]</i></p>
<dd> Specify which angle method calculation to use. The angle methods that are currently supported by <i>ipraytime</i> are,</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>1</code></p>
<dd> Egyptian General Authority of Survey<br />
&nbsp;<wbr>&nbsp;<wbr>Fajr/Isha Angle&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: 20/18<br />
&nbsp;<wbr>&nbsp;<wbr>Used in&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Africa, Indonesia, Iraq,&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Jordan, Lebanon, Malaysia,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Singapore, Syria,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Parts of the USA</p>
<dt><code>2</code></p>
<dd> University of Islamic Sciences, Karachi (Shaf&#8217;i)<br />
&nbsp;<wbr>&nbsp;<wbr>Fajr/Isha Angle&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: 18/18<br />
&nbsp;<wbr>&nbsp;<wbr>Used in&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Iran, Kuwait,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Parts of Europe</p>
<dt><code>3</code></p>
<dd> University of Islamic Sciences, Karachi (Hanafi)<br />
&nbsp;<wbr>&nbsp;<wbr>Fajr/Isha Angle&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: 18/18<br />
&nbsp;<wbr>&nbsp;<wbr>Used in&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Afghanistan, Bangladesh,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>India</p>
<dt><code>4</code></p>
<dd> Islamic Society of North America<br />
&nbsp;<wbr>&nbsp;<wbr>Fajr/Isha&nbsp;<wbr>&nbsp;<wbr>Angle&nbsp;<wbr>&nbsp;<wbr>: 15/15<br />
&nbsp;<wbr>&nbsp;<wbr>Used in&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Canada, Parts of UK,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Parts of USA</p>
<dt><code>5</code></p>
<dd> Muslim World League (MWL)<br />
&nbsp;<wbr>&nbsp;<wbr>Fajr/Isha&nbsp;<wbr>&nbsp;<wbr>Angle&nbsp;<wbr>&nbsp;<wbr>: 18/17<br />
&nbsp;<wbr>&nbsp;<wbr>Used in&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Parts of Europe,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Far East, Parts of USA</p>
<dt><code>6</code></p>
<dd> Umm Al-Qurra University<br />
&nbsp;<wbr>&nbsp;<wbr>Fajr/Isha Angl e&nbsp;<wbr>&nbsp;<wbr>: 19/0<br />
&nbsp;<wbr>&nbsp;<wbr>Isha Interval&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: 90 minutes from Al-Maghrib<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>prayer but set to 120<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>during Ramadan.<br />
&nbsp;<wbr>&nbsp;<wbr>Used in&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Saudi Arabia</p>
<dt><code>7</code></p>
<dd> Fixed Isha Angle Interval (always 90)<br />
&nbsp;<wbr>&nbsp;<wbr>Fajr/Isha Angle&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: 19.5/0<br />
&nbsp;<wbr>&nbsp;<wbr>Isha Interval&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: 90 minutes from Al-Maghrib<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>prayer<br />
&nbsp;<wbr>&nbsp;<wbr>Used in&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Bahrain, Oman, Qatar, UAE</p>
<dt><code>8</code></p>
<dd> Egyptian General Authority of Survey (Egypt)<br />
&nbsp;<wbr>&nbsp;<wbr>Fajr/Isha Angle&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: 19.5/17.5<br />
&nbsp;<wbr>&nbsp;<wbr>Used in&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>: Egypt</dl>
</dl>
<dt><code>-fa, &#8211;fajrangle </code><i>[real_num]</i></p>
<dd> Specify which angle to use for Fajr. Will override the one set by the &#8211;anglemethod.</p>
<dt><code>-ia, &#8211;ishaangle </code><i>[real_num]</i></p>
<dd> Specify which angle to use for Isha. Will override the one set by the &#8211;anglemethod.</p>
<dt><code>-s, &#8211;dst </code><i>[int_num]</i></p>
<dd> By default, <code>ipraytime</code> uses the host&#8217;s machine timezone information to determine whether daylight saving time is in effect or not. If this information is unavailable or not accurate, this option provides the means to explicitly set the DST status. Set this to 0 to completely disable daylight saving time. Set it to 1 to always add one hour to the computed prayer times.</dl>
<p> <code>-ss, &#8211;dst-start </code><i>yyyymmdd</i><br />
 <code>-se, &#8211;dst-end </code><i>yyyymmdd</i> </p>
<dl>
<dt>
<dd> Specify a range of dates where day light saving time is in effect for your location. For example:</dl>
<dl>
<dt>
<dd>
<dl>
<dt>ipraytime &#8211;dst-start 20040328 &#8211;dst-end 20041029</p>
<dd></dl>
</dl>
<dl>
<dt><code>-m, &#8211;month </code><i>[int_num]</i></p>
<dd> Specify to print either current month&#8217;s schedule or the passed-in value&#8217;s month schedule.</p>
<dt><code>-y, &#8211;year </code><i>[int_num]</i></p>
<dd> Specify to print either current year&#8217;s schedule or the passed-in value&#8217;s year schedule.</p>
<dt><code>-f, &#8211;file </code><i>pref_file</i></p>
<dd> Specify filename to load which contains user&#8217;s settings and preferences.</p>
<dt><code>-e, &#8211;end</code></p>
<dd> Specify to continue with schedule printing until the end of specified month.</p>
<dt><code>-b, &#8211;brief</code></p>
<dd> Specify to print a brief one-liner output for single day mode.</p>
<dt><code>-h12, &#8211;regular-hour</code></p>
<dd> Display the prayer times in regular time instead of military time.</p>
<dt><code>-r, &#8211;round </code><i>[int_num]</i></p>
<dd> Specify a method for rounding seconds. The supported methods are,</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>0</code></p>
<dd> No Rounding. Completely ignore the computed seconds value.</p>
<dt><code>1</code></p>
<dd> Regular Rounding. If seconds are equal to 30 or above, add 1 minute.</p>
<dt><code>2</code></p>
<dd> Special Rounding. Similar to regular rounding but we always round down for Shurooq and Imsaak times. (This is the default method)</p>
<dt><code>3</code></p>
<dd> Aggressive Rounding. Similar to Special Rounding but we add 1 minute if the seconds value are equal to 1 second or more.</dl>
</dl>
<dt><code>-x, &#8211;extreme </code><i>[int_num]</i></p>
<dd> Specify a method for prayer times calculations at high (49+) or extreme (66+) latitudes. Prayer times calculations relies heavily on astronomical events. At these latitudes some of those events do not occur at all, or are impossible to precisely calculate using conventional means. For example, at certain locations the sun never moves below the horizon to the position of the amount of Fajr angle degrees specified, therefore there will be no real Fajr time at that location. The supported extreme methods are:</p>
<dl>
<dt>
<dd>
<p> <code>Note:</code> Methods that have the <code>If Invalid</code> keyword are applied only when <code>ipraytime</code> is unable to calculate these times. Methods that have the <code>Always</code> keyword are applied always.</p>
<dl>
<dt><code>0</code></p>
<dd> None. If unable to calculate, leave as 99:99</p>
<dt><code>1</code></p>
<dd> Nearest Latitude (Aqrab Al-Bilaad): All prayers [Always]</p>
<dt><code>2</code></p>
<dd> Nearest Latitude (Aqrab Al-Bilaad): Fajr and Isha [Always]</p>
<dt><code>3</code></p>
<dd> Nearest Latitude (Aqrab Al-Bilaad): All prayers [If Invalid]</p>
<dt><code>4</code></p>
<dd> Nearest Good Day (Aqrab Al-Ayyam): All prayers [Always]</p>
<dt><code>5</code></p>
<dd> Nearest Good Day (Aqrab Al-Ayyam): All prayers [If Invalid] (This is the default method)</dl>
<p> <code>Note: </code> All the extreme methods following below do not have a proof in traditional Shari&#8217;a (Fiqh) resources. These methods were introduced by modern day Muslim scholars and scientists for practical reasons only.</p>
<dl>
<dt><code>6</code></p>
<dd> Seventh of Night: Fajr and Isha [Always]</p>
<dt><code>7</code></p>
<dd> Seventh of Night: Fajr and Isha [If Invalid]</p>
<dt><code>8</code></p>
<dd> Seventh of Day: Fajr and Isha [Always]</p>
<dt><code>9</code></p>
<dd> Seventh of Day: Fajr and Isha [If Invalid]</p>
<dt><code>10</code></p>
<dd> Half of the Night: Fajr and Isha [Always]</p>
<dt><code>11</code></p>
<dd> Half of the Night: Fajr and Isha [If Invalid]</dl>
<p> <code>Note: </code> To use the next two methods, you will need to specify <code>FajrInterval</code> and <code>IshaInterval</code> in your configuration file.</p>
<dl>
<dt><code>12</code></p>
<dd> Minutes from Shorooq/Maghrib: Fajr and Isha [Always]</p>
<dt><code>13</code></p>
<dd> Minutes from Shorooq/Maghrib: Fajr and Isha [If invalid]</dl>
</dl>
</dl>
<h2>CONFIGURATION</h2>
<p> <code>ipraytime</code> is capable of loading settings from a configuration file (<i>~/.iprayrc</i>). The default location of the configuration file can be changed using the &#8211;file option. The content of the file should be in the following syntax, `variable_string: value&#8217;. See the EXAMPLES section for usage examples. Below is a list of all supported settings which can be used in the configuration file:</p>
<h3>Location Settings</h3>
<dl>
<dt><code>City</code></p>
<dd> Specifies an informational city name string to be displayed for reference</p>
<dt><code>Latitude</code></p>
<dd> Specify the latitude setting to use during calculations. The value could be any real number</p>
<dt><code>Longitude</code></p>
<dd> Specify the longitude setting to use during calculations. The value could be any real number</p>
<dt><code>UTC</code></p>
<dd> Specify the difference between the specified timezone and that of GMT/UTC. The value could be any real number</p>
<dt><code>SeaLevel</code></p>
<dd> Specify height above Sea level (in meters)</p>
<dt><code>Pressure</code></p>
<dd> Specify the atmospheric pressure in millibars. The default value is 1010.</p>
<dt><code>Temperature</code></p>
<dd> Specify the temperature in Celsius degree. The default value is 10.</dl>
<h3>Calculation Method Settings</h3>
<dl>
<dt><code>AngleMethod</code></p>
<dd> Specify which angle method calculation to use. The value needs to be a positive integer of one of the supported methods. See the &#8211;anglemethod option for more information.</p>
<dt><code>Mathhab</code></p>
<dd> Specify which mathhab to use in one&#8217;s calculations. The current supported value are 1 for Shaf&#8217;i and 2 for Hanafi</p>
<dt><code>OffsetList</code></p>
<dd> Specify a list of values in minutes to add or subtract any amount of minutes from the daily computed prayer times. For example, If you want to add 30 seconds to Maghrib and subtract 2 minutes from Isha, you will set this option to `0 0 0 0 0.5 -2&#8242;.</p>
<dt><code>FajrAngle</code></p>
<dd> Specify the fajr angle to use during calculations. Will override the values of the specified method.</p>
<dt><code>IshaAngle</code></p>
<dd> Specify the isha angle to use during calculations. Will override the values of the specified method.</p>
<dt><code>ImsaakAngle</code></p>
<dd> Specify imsaak and fajr angle difference. The default value is 1.5 degrees.</p>
<dt><code>FajrInterval</code></p>
<dd> Specify the number of minutes between fajr and shorooq. This should be a positive integer.</p>
<dt><code>IshaInterval</code></p>
<dd> Specify the number of minutes between Isha and Maghrib. This should be a positive integer.</p>
<dt><code>ImsaakInterval</code></p>
<dd> Specify a difference in minutes between imsaak and fajr. The default Imsaak interval from fajr is 10 minutes if the FajrInterval is set.</p>
<dt><code>ExtremeMethod</code></p>
<dd> Specify which method to use for high and extreme latitudes. The value needs to be an integer of one of the supported extreme methods. See descriptions of the &#8211;extreme option for a list of the supported methods.</p>
<dt><code>NearestLatitude</code></p>
<dd> Specify the latitude Used for the `Nearest Latitude&#8217; extreme methods. The default is at 48.5 degrees.</p>
<dt><code>RoundMethod</code></p>
<dd> Specify which method to use for rounding seconds. The value needs to be an integer of one of the supported rounding methods. See the &#8211;round option for a list of the supported methods.</dl>
<h3>Daylight Saving Time Settings</h3>
<dl>
<dt><code>DST</code></p>
<dd> Specify the current DST status. Set this to 0 to completely disable daylight saving time. Or set it to 1 to always add one hour to the computed prayer times. See the &#8211;dst option for more information.</p>
<dt><code>DST-Start</code></p>
<dd> Specify the start date when daylight saving time adjustment is in effect for your location. This value should be a valid date in yyyymmdd form</p>
<dt><code>DST-End</code></p>
<dd> Specify the date when daylight saving time adjustment period ends. This value should be a valid date in yyyymmdd form</dl>
<h3>Display Settings</h3>
<dl>
<dt><code>HourFormat</code></p>
<dd> Specify a time format for displaying the prayer times. The value should be 12 (regular time) or 24 (military time)</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>IPT_DATA</code></p>
<dd> One means to pass-in the various required settings is via this variable. The format of the variable needs to be &quot;LocationName Latitude Longitude UTCdiff AngleMethodNumber&quot;. For instance, setenv IPT_DATA &quot;Dubai 25.25 55.3 4 2&quot;</dl>
<h2>FILES</h2>
<p> <i>~/.iprayrc</i> User configuration file.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>A sample (<code>~/.iprayrc</code>) showing how options are set:</p>
<dd>
<pre>
City: Brussels, Belguim
Latitude: 50.8333
Longitude: 4.3333
UTC: 1
AngleMethod: 2
Mathhab: 1
OffsetList: 0 0 1 2.21 3 -1
</pre>
<dt>Examples of using the command line options:</p>
<dd>
<pre>
ipraytime -y 2007
ipraytime -lat 29.5000 -lon 47.7500 -u 3 --anglemethod 2 -d 20071229 -h12
</pre>
</dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs on the web using <a rel="nofollow" href="http://bugs.arabeyes.org">http://bugs.arabeyes.org</a></p>
<h2>AUTHORS</h2>
<p> Written by Nadim Shaikli and Thamer Mahmoud. Part of the Arabeyes.org project.</p>
<h2>COPYRIGHT</h2>
<p> <code>ipraytime</code> is subject to the GNU General Public License (GPL).<br />
 Copyright &#169; 2005, Arabeyes, Nadim Shaikli.</p>
<h2>SEE ALSO</h2>
<p> The ITL library (libitl) from the Islamic Tools and Libraries project. It is the underlying requirement for <code>ipraytime</code> to function. The ITL library was created and is hosted at <code><a rel="nofollow" href="http://www.arabeyes.org">www.arabeyes.org</a></code>. </p>
<h2>Index</h2>
