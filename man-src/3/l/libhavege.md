---
title: "libhavege(3)"
name: "libhavege"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libhavege/"
description: "libhavege, havege_create, havege_run, havege_rng, havege_destroy, havege_status, havege_status_dump, havege_version – haveged RNG"
---

<h2>NAME</h2>
<p> libhavege, havege_create, havege_run, havege_rng, havege_destroy, havege_status, havege_status_dump, havege_version &#8211; haveged RNG</p>
<h2>SYNOPSIS</h2>
<dl>
<dt></dl>
<pre><code>
#include &lt;haveged/havege.h&gt;
H_PARAMS params = {0};
h_status status;
char status_buf[512];
if (NULL == havege_version(HAVEGE_PREP_VERSION))
    exit(1);
H_PTR handle = havege_create(&amp;params);
havege_status(handle, &amp;status);
havege_run(handle);
rc = havege_rng(handle, handle-&gt;io_buf, handle-&gt;i_readSz / sizeof(H_UINT));
havege_status_dump(handle, H_SD_TOPIC_BUILD, status_buf, sizeof(status_buf));
havege_destroy(handle);
</code></pre>
<p>&nbsp;<wbr></p>
<h2>DESCRIPTION</h2>
<p> The libhavege library provides the haveged random number generator and it&#8217;s associated tuning and testing facilities in a development sub-package. All haveged conditional build features are preserved and all haveged options not directly related to it&#8217;s daemon or file system interfaces are available. This means that the same haveged tuning and testing components are present in the library with the equivalent controls provided by the haveged command line. </p>
<h2>API METHODS</h2>
<p> The libhavege library uses the opaque handle technique to manage it&#8217;s required resources. Errors are returned in the &quot;error&quot; member of the handle. The havege_destroy() method should be called to dispose of any resources claimed by havege_create(). </p>
<p> <code>H_PTR havege_create(H_PARAMS </code><i>*params</i><code>);</code> </p>
<p> Create an anchor. Most members of the H_PARAMS input to this call correspond closely to haveged command line options (see <code><a href="/docs/linux/man/8-haveged/">haveged</a>(8)</code> for details). The caller should check for a non-null return value with a error value of H_NOERR. Any non-null return should be disposed of by a call to havege_destroy() to free any resources. Possible error values: H_NOERR, H_NOTESTSPEC, H_NOBUF, H_NOTESTMEM, H_NOINIT </p>
<p> <code>void havege_destroy(H_PTR </code><i>hptr</i><code>);</code> </p>
<p> Free all allocated anchor resources. If the multi-core option is used, this method should be called from a signal handler to prevent zombie processes. If called by the process that called haveged_create(), hptr will be freed when all child processes (if any) have terminated. If called by a child process, H_EXIT will be set and all children awakened to exit. </p>
<p> <code>int havege_rng(H_PTR </code><i>hptr</i><code>, H_UINT </code><i>*buf</i><code>, H_UINT </code><i>sz</i><code>);</code> </p>
<p> Read random bytes from an active anchor. The RNG must have been previously readied by a call to havege_run(). The read must take place within the allocated buffer, hptr-&gt;io_buf. The range specified is the number of H_UINT to read. If the multi-core option is used, this buffer is memory mapped between collectors. Possible error values: H_NOERR, H_NOTESRUN, H_NOPOST, H_NODONE, H_NORQST, H_NOCOMP, H_EXIT </p>
<p> <code>int havege_run(H_PTR </code><i>hptr</i><code>);</code> </p>
<p> Warm up the RNG and run the start-up tests. The operation succeeded if the error member of the handle is H_NOERR. A failed handle should be disposed of by a call to havege_destroy(). Possible error values: H_NOERR, H_NOCOLLECT, H_NOWALK, H_NOTESTMEM, H_NOTASK, H_NOTESTTOT, H_NOWAIT, H_NOTIMER, and any havege_rng() error. </p>
<p> <code>void havege_status(H_PTR </code><i>hptr</i><code>, H_STATUS </code><i>hsts</i><code>);</code><br />
&nbsp;<wbr> Fills in the h_status structure with read-only information collected from the package build, run-time tuning, and test components.<br />
&nbsp;<wbr> </p>
<p> <code>int havege_status_dump(H_PTR </code><i>hptr</i><code>, H_SD_TOPIC </code><i>topic</i><code>, char </code><i>*buf</i><code>, size_t </code><i>len</i><code>);</code> </p>
<p> Calls havege_status() and formats standard presentations of havege status in the supplied buffer. The standard formats are: </p>
<dl>
<dt>
<dd> H_SD_TOPIC_BUILD </p>
<p> ver: %s; arch: %s; vend: %s; build: (%s); collect: %dK </p>
<p> H_SD_TOPIC_TUNE </p>
<p> cpu: (%s); data: %dK (%s); inst: %dK (%s); idx: %d/%d; sz: %d/%d </p>
<p> H_SD_TOPIC_TEST </p>
<p> [tot tests(%s): A:%d/%d B: %d/%d;][continuous tests(%s): A:%d/%d B: %d/%d;][last entropy estimate %g] </p>
<p> H_SD_TOPIC_SUM </p>
<p> fills: %d, generated: %.4g %c bytes</dl>
<p> <code>const char *havege_version(const char *</code><i>version</i><code>);</code><br />
&nbsp;<wbr> Return/check library prep version. The prep version is the package version used to build the library. A null argument returns the prep version unconditionally. Using the definition of the prep string in havege.h as input returns the prep version if the header file is compatible with the library, or NULL if it is not. Intended to be called before attempting any initialization. </p>
<h2>NOTES</h2>
<p> The sizes of the processor level 1 instruction and data caches are used to tune the HAVEGE algorithm for maximum sensitivity. If these sizes not specified, haveged will attempt to determine the sizes dynamically from the Linux sysfs and/or cpuid instruction with a fallback to a compiled default if no better information is not available. </p>
<p> The haveged RNG includes a run time test facility based upon the test suite defined in the AIS-31 specification from the The German Federal Office for Information Security (Bundesamt für Sicherheit in der Informationstechnik). The test suite consists of 11 statistical tests packaged into two test suites (&quot;A&quot; and &quot;B&quot;). The tests can be run at initialization (a.k.a. a &quot;tot&quot; test), or continuously to monitor all output. Failure of a suite will abort operation unless the behavior is explicitly waived in the test setup options. </p>
<p> Procedure A contains 6 test procedures designed to ensure statistically inconspicuous behavior. The first test, &quot;test0&quot;, checks the disjointedness of 65k six-bit strings. The remainder of the procedure consists of 257 repetitions of the FIPS140-1 tests, &quot;test1&quot; through &quot;test4&quot;, and an auto-correlation test, &quot;test5&quot;. The fixed size of the Procedure A input makes it ideal for continuous use, but the procedure is slow and resource intensive. In particular, test5 is several orders of magnitude slower than any other individual AIS test. As an alternative for those who cannot tolerate this load, procedure A variants A&lt;n&gt; are provided that execute all included tests but execute test5 only every 2^n repetitions. Even with this accommodation, procedure A is much slower than procedure B. </p>
<p> Procedure B contains 5 tests, &quot;test6a&quot;, &quot;test6b&#8217;, &quot;test7a&quot;, &quot;test7b&quot;, and &quot;test8&quot;. The first 4 tests verify the expected frequencies for samples 100,000 one-step, two-step, three-step, and four-step bit transitions. The last test provides an empirical entropy estimate of the input. The input required to complete these tests is variable, resulting in an ever-shifting bit alignment that guards against buffering artifacts. </p>
<p> Each test procedure requires more than 1MB of data. Test input is managed by a bit index into the collection buffer. An independent index manages where integer output is taken from the same buffer. A buffer fill is triggered when the output index indicates all data has been extracted from the buffer. Online testing takes place after the buffer has been refilled but before the output index update allows output to resume. If any online test fails while processing the buffer, the buffer will be refilled and reprocessed until any retry is complete and the buffer contains no failed online tests or the online test procedure has failed and the RNG is considered broken. </p>
<p> It is recommend to run both AIS test procedures at start-up to ensure the RNG is properly initialized. If resources are in short supply, omitting procedure A will save memory and time, with little risk in circumstances where output is mixed with other sources in /dev/random or other csprng. Continuous testing is also recommended where the throughput penalty is acceptable. One recent assessment of testing throughput costs is shown below. </p>
<dl>
<dt>
<dd>
<dl>
<dt>haveged -n0 -oc | pv &gt; /dev/null</p>
<dd> 400MiB/s</p>
<dt>haveged -n0 -ocb | pv &gt; /dev/null</p>
<dd> 70MiB/s</p>
<dt>haveged -n0 -oca8b | pv &gt; /dev/null</p>
<dd> 13MiB/s</p>
<dt>haveged -n0 -oca8 | pv &gt; /dev/null</p>
<dd> 8MiB/s</p>
<dt>haveged -n0 -oca | pv &gt; /dev/null</p>
<dd> 100kiB/s</dl>
</dl>
<p> Continuous testing also exposes another possible pitfall. Even an ideal RNG has a 10e-4 chance of failing either test procedure. The strict retry policy of AIS-31 is designed to guarantee an ideal RNG will &quot;almost never&quot; fail a test procedure. A single retry is mandated only to recover from a previous attempt that experienced a single individual test failure. The haveged implementation logs all retries and terminates on test procedure failures unless the procedure has been flagged as advisory by the &quot;w&quot; argument (see &#8211;onlinetest in <code><a href="/docs/linux/man/8-haveged/">haveged</a>(8)</code> ). Little evidence of the retry mechanism is seen unless large data sets are processed. Procedure A is too slow to be practical in these situations, so procedure B has been the best studied. Retries are observed at the approximate rate of 0.7-0.8 failures/GB, mostly in the test7 multi-step transition checks. </p>
<p> The probability that procedureB will fail two times in a row (in which case the program will be terminated unless w option was specified) is 4e-7 which is expected to happen at an approximate rate of once per 3,000 TB. When producing large amounts of data in order of TBs it&#8217;s recommended to use -w option to make sure that program will not prematurely terminate because of a failed retry and carefully examine the stderr output for any problems. </p>
<h2>FILES</h2>
<p> Tuning information may be extracted from the following virtual file paths if tuning is required and the path exists. </p>
<dl>
<dt>
<dd> <i>/proc/cpuinfo</i> </p>
<p> <i>/proc/self/status</i> </p>
<p> <i>/sys/devices/system/cpu/online</i> </p>
<p> <i>/sys/devices/system/cpu/cpu%d/cache/index%d/level</i></dl>
<h2>DIAGNOSTICS</h2>
<p> To enable diagnostic output, supply a msg_out callback when creating the handle. All possible errors are enumerated in havege.h and reproduced here for reference. </p>
<p> <code>01 H_NOHANDLE</code></p>
<dl>
<dt>
<dd> No memory for handle </p>
</dl>
<p> <code>02 H_NOBUF</code></p>
<dl>
<dt>
<dd> Output buffer allocation failed </p>
</dl>
<p> <code>03 H_NOINIT</code></p>
<dl>
<dt>
<dd> Semaphore init failed </p>
</dl>
<p> <code>04 H_NOCOLLECT</code></p>
<dl>
<dt>
<dd> Collector allocation failed </p>
</dl>
<p> <code>05 H_NOWALK</code></p>
<dl>
<dt>
<dd> Walk buffer allocation failed </p>
</dl>
<p> <code>06 H_NOTESTSPEC</code></p>
<dl>
<dt>
<dd> Invalid test specification </p>
</dl>
<p> <code>07 H_NOTESTINIT</code></p>
<dl>
<dt>
<dd> Test setup failed </p>
</dl>
<p> <code>08 H_NOTESTMEM</code></p>
<dl>
<dt>
<dd> Unable to allocate test memory </p>
</dl>
<p> <code>09 H_NOTESTTOT</code></p>
<dl>
<dt>
<dd> Power on (i.e. &#8216;tot&#8217;) test failed </p>
</dl>
<p> <code>10 H_NOTESTRUN</code></p>
<dl>
<dt>
<dd> Continuous test failed </p>
</dl>
<p> <code>11 H_NOCORES</code></p>
<dl>
<dt>
<dd> Too many cores specified </p>
</dl>
<p> <code>12 H_NOTASK</code></p>
<dl>
<dt>
<dd> Unable to create child task </p>
</dl>
<p> <code>13 H_NOWAIT</code></p>
<dl>
<dt>
<dd> sem_wait failed </p>
</dl>
<p> <code>14 H_NOPOST</code></p>
<dl>
<dt>
<dd> sem_post failed </p>
</dl>
<p> <code>15 H_NODONE</code></p>
<dl>
<dt>
<dd> sem_post done failed </p>
</dl>
<p> <code>16 H_NORQST</code></p>
<dl>
<dt>
<dd> sem_post request failed </p>
</dl>
<p> <code>17 H_NOCOMP</code></p>
<dl>
<dt>
<dd> wait for completion failed </p>
</dl>
<p> <code>18 H_EXIT</code></p>
<dl>
<dt>
<dd> Exit signal </p>
</dl>
<p> <code>19 H_NOTIMER</code></p>
<dl>
<dt>
<dd> Timer failed </p>
</dl>
<h2>EXAMPLE</h2>
<p> The following minimal program writes the contents of 16 collection buffers of random data to stdout with continuous testing. </p>
<pre><code>
#include &lt;haveged/havege.h&gt;
#include &lt;stdio.h&gt;
int main(void)
{
    H_PTR havege_state;
    H_PARAMS havege_parameters = {0};
    int i, rc;
    if (NULL == havege_version(HAVEGE_PREP_VERSION)) {
        fprintf(stderr, "Incompatible library %s
", havege_version(NULL));
        return 1;
    }
    havege_parameters.testSpec = "ta8bcb";
    havege_state = havege_create(&amp;havege_parameters);
    rc = havege_state == NULL ? H_NOHANDLE : havege_state-&gt;error;
    if (H_NOERR == rc) {
        if (0 == havege_run(havege_state)) {
            H_UINT *buf = havege_state-&gt;io_buf;
            int size = havege_state-&gt;i_readSz / sizeof(H_UINT);
            char info[256];
            for (i = 0; i &lt; 16; i++) {
                rc = havege_rng(havege_state, buf, size);
                if (rc != size) {
                    fprintf(stderr, "RNG read failed %d
", havege_state-&gt;error);
                    break;
                }
                rc = fwrite(buf, 1, size * sizeof(H_UINT), stdout);
                if (rc &lt; size) {
                    fprintf(stderr, "Write failed
");
                    break;
                }
            }
            i = havege_status_dump(havege_state, H_SD_TOPIC_TEST, info, sizeof(info));
            info[i++] = '
';
            havege_status_dump(havege_state, H_SD_TOPIC_SUM, info + i, sizeof(info) - i);
            fprintf(stderr, "%s
", info);
        } else
            fprintf(stderr, "Initialize failed %d
", havege_state-&gt;error);
        havege_destroy(havege_state);
    } else
        fprintf(stderr, "Create failed %d
", rc);
    return rc;
}
</code></pre>
<p> Defaults are provided for all inputs to havege_create() as documented in havege.h. In this case for example, (16*4kb=65kb) will be written to stdout because the default size for i_readsz in 4kb. </p>
<h2>SEE ALSO</h2>
<dl>
<dt><code><a href="/docs/linux/man/8-haveged/">haveged</a>(8)</code></p>
<dd>
</dl>
<h2>REFERENCES</h2>
<p> <code><a href="/docs/linux/man/8-haveged/">haveged</a>(8)</code> references provides a basic reading list. The following links are suggested as sources for further exploration.</p>
<dl>
<dt>The origins of the HAVEGE concept can be found at:</p>
<dd> <a rel="nofollow" href="http://www.irisa.fr/caps/projects/hipsor/">http://www.irisa.fr/caps/projects/hipsor/</a></p>
<dt>Tuning concepts inspired by (the complexity) at:</p>
<dd> <a rel="nofollow" href="http://www.open-mpi.org/projects/hwloc/">http://www.open-mpi.org/projects/hwloc/</a></p>
<dt>Reference documentation for the AIS-31 test suite can be found at:</p>
<dd> <a rel="nofollow" href="https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Zertifizierung/Interpretationen/AIS_31_Functionality_classes_for_random_number_generators_e.pdf?__blob=publicationFile">https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Zertifizierung/Interpretationen/AIS_31_Functionality_classes_for_random_number_generators_e.pdf?__blob=publicationFile</a></p>
<dt>Implementation and design information available at:</p>
<dd> <a rel="nofollow" href="http://www.issihosts.com/haveged/">http://www.issihosts.com/haveged/</a> </p>
</dl>
<h2>AUTHORS</h2>
<p> Gary Wuertz &lt;gary [at] issiweb.com&gt; and Jirka Hladky &lt;hladky jiri AT gmail DOT com&gt; </p>
<h2>Index</h2>
