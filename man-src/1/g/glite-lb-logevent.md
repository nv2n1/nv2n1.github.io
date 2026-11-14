---
title: "glite-lb-logevent(1)"
name: "glite-lb-logevent"
section: "1"
letter: "g"
url: "/docs/linux/man/1-glite-lb-logevent/"
description: "glite-lb-logevent – program for logging events to L&B subsystem"
---

<h2 class="name">NAME</h2>
<p> glite-lb-logevent &#8211; program for logging events to L&amp;B subsystem</p>
<h2>SYNOPSIS</h2>
<p> <code>glite-lb-logevent</code> <code>-s Application -e UserTag</code> <code>-j</code> <i>JOBID </i> <code>-c</code> <i>SEQCODE </i> <code>&#8211;name </code> <i>NAME</i> <code>&#8211;value</code> <i>VALUE</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>glite-lb-logevent </code> is a low-level program for logging events to the L&amp;B service. It is used internally by WMS components and has many more options, that are not recomend to be used at the user level. At the user level it is supposed to be used only for logging user tag events. </p>
<h2>USAGE</h2>
<p> Besides <i>NAME</i> and <i>VALUE</i> of the tag, which are user defined, the user has to specify a valid <i>JOBID</i>, and <i>SEQCODE</i> (L&amp;B event sequence code). </p>
<p> The user application is always executed from within a <i>JobWrapper</i> script. The wrapper sets the appropriate JobId in the environment variable EDG_WL_JOBID. The user should pass this value to the -j option of <code>glite-lb-logevent.</code> </p>
<p> Similarly, the wrapper sets an initial value of the event sequence code in the environment variable EDG_WL_SEQUENCE_CODE. If the user application calls <code>glite-lb-logevent</code> just once, it is sufficient to pass this value to the -c option. However, if there are more subsequent calls, the user is responsible for capturing an updated sequence code from the <code>stdout</code> of <code>glite-lb-logevent</code> and using it in subsequent calls. The L&amp;B design requires the sequence codes in order to be able to sort events correctly while not relying on strictly synchronized clocks. </p>
<h2>EXAMPLE</h2>
<p> The example bellow is a job consisting of 100 phases. A user tag <i>phase</i> is used to log the phase currently being executed. Subsequently, the user may monitor execution of the job phases as a part of the job status returned by L&amp;B. </p>
<pre><code>
#!/ bin / sh
for
    p in `seq 1 100`;
do
#log the UserTag event
EDG_WL_SEQUENCE_CODE =`glite - lb - logevent - s Application - e UserTag - j $EDG_WL_JOBID - c $EDG_WL_SEQUENCE_CODE-- name = phase-- value = $p`
#do the actual computation here
    done
</code></pre>
<h2>OTHER OPTIONS</h2>
<p> See command line help (glite-lb-logevent -h) for extensive help on all options. However, EDG users should should follow the usage shown in SYNOPSIS strictly. Logging other events may confuse the L&amp;B service and cause wrong job status information to be reported. </p>
<h2>FILES</h2>
<p> No configuration files needed. </p>
<h2>BUGS</h2>
<p> Please report all bugs to CESNET gLite L&amp;B issue tracker available at <i><a rel="nofollow" href="https://github.com/CESNET/glite-lb/issues">https://github.com/CESNET/glite-lb/issues</a></i> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-glite-lb-bkserverd/">glite-lb-bkserverd</a></code>(8), <a href="/docs/linux/man/8-glite-lb-interlogd/">glite-lb-interlogd</a>(8), <a href="/docs/linux/man/8-glite-lb-logd/">glite-lb-logd</a>(8) </p>
<h2>AUTHOR</h2>
<p> EU EGEE, JRA1. </p>
<h2>Index</h2>
