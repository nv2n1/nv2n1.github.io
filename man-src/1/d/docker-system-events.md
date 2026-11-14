---
title: "docker-system-events(1)"
name: "docker-system-events"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-system-events/"
description: "docker-system-events – Get real time events from the server"
---

<h2 class="name">NAME</h2>
<p> docker-system-events &#8211; Get real time events from the server </p>
<h2>SYNOPSIS</h2>
<p> <code>docker system events [OPTIONS]</code> </p>
<h2>DESCRIPTION</h2>
<p> Get event information from the Docker daemon. Information can include historical information and real-time information. </p>
<p> Docker containers will report the following events: </p>
<dl>
<dt>
<dd>
<pre>
attach, commit, copy, create, destroy, detach, die, exec_create, exec_detach, exec_start, export, kill, oom, pause, rename, resize, restart, start, stop, top, unpause, update
</pre>
</dl>
<p> Docker images report the following events: </p>
<dl>
<dt>
<dd>
<pre>
delete, import, load, pull, push, save, tag, untag
</pre>
</dl>
<p> Docker volumes report the following events: </p>
<dl>
<dt>
<dd>
<pre>
create, mount, unmount, destroy
</pre>
</dl>
<p> Docker networks report the following events: </p>
<dl>
<dt>
<dd>
<pre>
create, connect, disconnect, destroy
</pre>
</dl>
<h2>OPTIONS</h2>
<p> The &#8211;since and &#8211;until parameters can be Unix timestamps, date formatted timestamps, or Go duration strings (e.g. 10m, 1h30m) computed relative to the client machine&#8217;s time. If you do not provide the &#8211;since option, the command returns only new and/or live events. Supported formats for date formatted time stamps include RFC3339Nano, RFC3339, 2006-01-02T15:04:05, 2006-01-02T15:04:05.999999999, 2006-01-02Z07:00, and 2006-01-02. The local timezone on the client will be used if you do not provide either a Z or a +-00:00 timezone offset at the end of the timestamp. When providing Unix timestamps enter seconds[.nanoseconds], where seconds is the number of seconds that have elapsed since January 1, 1970 (midnight UTC/GMT), not counting leap seconds (aka Unix epoch or Unix time), and the optional .nanoseconds field is a fraction of a second no more than nine digits long. </p>
<h2>EXAMPLES</h2>
<h2>Listening for Docker events</h2>
<p> After running docker events a container 786d698004576 is started and stopped (The container name has been shortened in the output below): </p>
<dl>
<dt>
<dd>
<pre>
# docker events
2015-01-28T20:21:31.000000000-08:00 59211849bc10: (from whenry/testimage:latest) start
2015-01-28T20:21:31.000000000-08:00 59211849bc10: (from whenry/testimage:latest) die
2015-01-28T20:21:32.000000000-08:00 59211849bc10: (from whenry/testimage:latest) stop
</pre>
</dl>
<h2>Listening for events since a given date</h2>
<p> Again the output container IDs have been shortened for the purposes of this document: </p>
<dl>
<dt>
<dd>
<pre>
# docker events --since '2015-01-28'
2015-01-28T20:25:38.000000000-08:00 c21f6c22ba27: (from whenry/testimage:latest) create
2015-01-28T20:25:38.000000000-08:00 c21f6c22ba27: (from whenry/testimage:latest) start
2015-01-28T20:25:39.000000000-08:00 c21f6c22ba27: (from whenry/testimage:latest) create
2015-01-28T20:25:39.000000000-08:00 c21f6c22ba27: (from whenry/testimage:latest) start
2015-01-28T20:25:40.000000000-08:00 c21f6c22ba27: (from whenry/testimage:latest) die
2015-01-28T20:25:42.000000000-08:00 c21f6c22ba27: (from whenry/testimage:latest) stop
2015-01-28T20:25:45.000000000-08:00 c21f6c22ba27: (from whenry/testimage:latest) start
2015-01-28T20:25:45.000000000-08:00 c21f6c22ba27: (from whenry/testimage:latest) die
2015-01-28T20:25:46.000000000-08:00 c21f6c22ba27: (from whenry/testimage:latest) stop
</pre>
</dl>
<p> The following example outputs all events that were generated in the last 3 minutes, relative to the current time on the client machine: </p>
<dl>
<dt>
<dd>
<pre>
# docker events --since '3m'
2015-05-12T11:51:30.999999999Z07:00  4386fb97867d: (from ubuntu-1:14.04) die
2015-05-12T15:52:12.999999999Z07:00  4386fb97867d: (from ubuntu-1:14.04) stop
2015-05-12T15:53:45.999999999Z07:00  7805c1d35632: (from redis:2.8) die
2015-05-12T15:54:03.999999999Z07:00  7805c1d35632: (from redis:2.8) stop
</pre>
</dl>
<p> If you do not provide the &#8211;since option, the command returns only new and/or live events. </p>
<h2>Format</h2>
<p> If a format (&#8211;format) is specified, the given template will be executed instead of the default format. Go&#8217;s <code>text/template</code> package describes all the details of the format. </p>
<dl>
<dt>
<dd>
<pre><code>
#docker events-- filter 'type=container' --format 'Type=&#123;&#123;.Type}}  Status=&#123;&#123;.Status}}  ID=&#123;&#123;.ID}}'
Type = container Status = create ID = 2ee349dac409e97974ce8d01b70d250b85e0ba8189299c126a87812311951e26 Type = container Status = attach ID = 2ee349dac409e97974ce8d01b70d250b85e0ba8189299c126a87812311951e26 Type = container Status = start ID = 2ee349dac409e97974ce8d01b70d250b85e0ba8189299c126a87812311951e26 Type = container Status = resize ID = 2ee349dac409e97974ce8d01b70d250b85e0ba8189299c126a87812311951e26 Type = container Status = die ID = 2ee349dac409e97974ce8d01b70d250b85e0ba8189299c126a87812311951e26 Type = container Status = destroy ID = 2ee349dac409e97974ce8d01b70d250b85e0ba8189299c126a87812311951e26
</code></pre>
</dl>
<p> If a format is set to &#123;&#123;json .}}, the events are streamed as valid JSON Lines. For information about JSON Lines, please refer to <a rel="nofollow" href="http://jsonlines.org/">http://jsonlines.org/</a> . </p>
<dl>
<dt>
<dd>
<p>#docker events&#8211; format &#8216;&#123;&#123;json .}}&#8217;<br />
{<br />
    &#8220;status&#8221; : &#8220;create&#8221;, &#8220;id&#8221; : &#8220;196016a57679bf42424484918746a9474cd905dd993c4d0f4..<br />
    {<br />
        &#8220;status&#8221; : &#8220;attach&#8221;, &#8220;id&#8221; : &#8220;196016a57679bf42424484918746a9474cd905dd993c4d0f4..<br />
        {<br />
            &#8220;Type&#8221; : &#8220;network&#8221;, &#8220;Action&#8221; : &#8220;connect&#8221;, &#8220;Actor&#8221;:<br />
            {<br />
                &#8220;ID&#8221; : &#8220;1b50a5bf755f6021dfa78e..<br />
                {<br />
                    &#8220;status&#8221; : &#8220;start&#8221;, &#8220;id&#8221; : &#8220;196016a57679bf42424484918746a9474cd905dd993c4d0f42..<br />
                    {<br />
                        &#8220;status&#8221; : &#8220;resize&#8221;, &#8220;id&#8221; : &#8220;196016a57679bf42424484918746a9474cd905dd993c4d0f4..
</dl>
<h2>Filters</h2>
<dl>
<dt>
<dd>
<pre><code>
$ docker events-- filter 'event=stop' 2014 - 05 - 10T17 : 42 : 14.999999999Z07 : 00 container stop 4386fb97867d(image = ubuntu - 1 : 14.04)2014 - 09 - 03T17 : 42 : 14.999999999Z07 : 00 container stop 7805c1d35632(image = redis : 2.8) $ docker events-- filter 'image=ubuntu-1:14.04' 2014 - 05 - 10T17 : 42 : 14.999999999Z07 : 00 container start 4386fb97867d(image = ubuntu - 1 : 14.04)2014 - 05 - 10T17 : 42 : 14.999999999Z07 : 00 container die 4386fb97867d(image = ubuntu - 1 : 14.04)2014 - 05 - 10T17 : 42 : 14.999999999Z07 : 00 container stop 4386fb97867d(image = ubuntu - 1 : 14.04) $ docker events-- filter 'container=7805c1d35632' 2014 - 05 - 10T17 : 42 : 14.999999999Z07 : 00 container die 7805c1d35632(image = redis : 2.8)2014 - 09 - 03T15 : 49 : 29.999999999Z07 : 00 container stop 7805c1d35632(image = redis : 2.8) $ docker events-- filter 'container=7805c1d35632' --filter 'container=4386fb97867d' 2014 - 09 - 03T15 : 49 : 29.999999999Z07 : 00 container die 4386fb97867d(image = ubuntu - 1 : 14.04)2014 - 05 - 10T17 : 42 : 14.999999999Z07 : 00 container stop 4386fb97867d(image = ubuntu - 1 : 14.04)2014 - 05 - 10T17 : 42 : 14.999999999Z07 : 00 container die 7805c1d35632(image = redis : 2.8)2014 - 09 - 03T15 : 49 : 29.999999999Z07 : 00 container stop 7805c1d35632(image = redis : 2.8) $ docker events-- filter 'container=7805c1d35632' --filter 'event=stop' 2014 - 09 - 03T15 : 49 : 29.999999999Z07 : 00 container stop 7805c1d35632(image = redis : 2.8) $ docker events-- filter 'type=volume' 2015 - 12 - 23T21 : 05 : 28.136212689Z volume create test - event - volume - local(driver = local) 2015 - 12 - 23T21 : 05 : 28.383462717Z volume mount test - event - volume - local(read / write = true, container = 562fe10671e9273da25eed36cdce26159085ac7ee6707105fd534866340a5025, destination = / foo, driver = local, propagation = rprivate) 2015 - 12 - 23T21 : 05 : 28.650314265Z volume unmount test - event - volume - local(container = 562fe10671e9273da25eed36cdce26159085ac7ee6707105fd534866340a5025, driver = local) 2015 - 12 - 23T21 : 05 : 28.716218405Z volume destroy test - event - volume - local(driver = local) $ docker events-- filter 'type=network' 2015 - 12 - 23T21 : 38 : 24.705709133Z network create 8b111217944ba0ba844a65b13efcd57dc494932ee2527577758f939315ba2c5b(name = test - event - network - local, type = bridge)2015 - 12 - 23T21 : 38 : 25.119625123Z network connect 8b111217944ba0ba844a65b13efcd57dc494932ee2527577758f939315ba2c5b(name = test - event - network - local, container = b4be644031a3d90b400f88ab3d4bdf4dc23adb250e696b6328b85441abe2c54e, type = bridge) $ docker events-- filter 'type=plugin'(experimental)2016 - 07 - 25T17 : 30 : 14.825557616Z plugin pull ec7b87f2ce84330fe076e666f17dfc049d2d7ae0b8190763de94e1f2d105993f(name = tiborvass / sample - volume - plugin
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  : latest) 2016 -
    07 - 25T17 : 30 : 14.888127370Z plugin enable ec7b87f2ce84330fe076e666f17dfc049d2d7ae0b8190763de94e1f2d105993f(name = tiborvass / sample - volume - plugin
                                                                                                                   : latest)
</code></pre>
</dl>
<h2>OPTIONS</h2>
<p> <code>-f</code>, <code>&#8211;filter</code>= <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Filter output based on conditions provided</p>
<p> <code>&#8211;format</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Format the output using the given Go template</p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for events</p>
<p> <code>&#8211;since</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Show all events created since timestamp</p>
<p> <code>&#8211;until</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Stream events until this timestamp</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-system/">docker-system</a>(1)</code> </p>
<h2>Index</h2>
