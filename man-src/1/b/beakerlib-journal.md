---
title: "beakerlib-journal(1)"
name: "beakerlib-journal"
section: "1"
letter: "b"
url: "/docs/linux/man/1-beakerlib-journal/"
---

<h2 class="name">NAME</h2>
 

 BeakerLib - journal - journalling functionality 

<h2>DESCRIPTION</h2>

 Routines for initializing the journalling features and pretty printing journal contents.

<h2>FUNCTIONS</h2>

<h3>Journalling</h3>

 <i>rlJournalStart</i> 

 Initialize the journal file. 

 <pre>
    rlJournalStart
</pre> 

 Run on the very beginning of your script to initialize journalling functionality. 

 <i>rlJournalEnd</i> 

 Summarize the test run and upload the journal file. 

 <pre>
    rlJournalEnd
</pre> 

 Run on the very end of your script to print summary of the whole test run, generate <font SIZE="-1">OUTPUTFILE</font> and include journal in Beaker logs. 

 <i>rlJournalPrint</i> 

 Print the content of the journal in pretty xml format. 

 <pre>
    rlJournalPrint [type]
</pre>
<dl>
<dt>type
<dd> Can be either 'raw' or 'pretty', with the latter as a default. Raw: xml is in raw form, no indentation etc Pretty: xml is pretty printed, indented, with one record per line</dl>
 

 Example: 

 <pre><code>
    &lt;?xml version="1.0"?&gt;
    &lt;BEAKER_TEST&gt;
      &lt;test_id&gt;debugging&lt;/test_id&gt;
      &lt;package&gt;setup&lt;/package&gt;
      &lt;pkgdetails&gt;setup-2.8.9-1.fc12.noarch&lt;/pkgdetails&gt;
      &lt;starttime&gt;2010-02-08 15:17:47&lt;/starttime&gt;
      &lt;endtime&gt;2010-02-08 15:17:47&lt;/endtime&gt;
      &lt;testname&gt;/examples/beakerlib/Sanity/simple&lt;/testname&gt;
      &lt;release&gt;Fedora release 12 (Constantine)&lt;/release&gt;
      &lt;hostname&gt;localhost&lt;/hostname&gt;
      &lt;arch&gt;i686&lt;/arch&gt;
      &lt;purpose&gt;PURPOSE of /examples/beakerlib/Sanity/simple
        Description: Minimal BeakerLib sanity test
        Author: Petr Splichal &amp;lt;psplicha [at] redhat.com&amp;gt;
        This is a minimal sanity test for BeakerLib. It contains a single
        phase with a couple of asserts. We Just check that the "setup"
        package is installed and that there is a sane /etc/passwd file.
      &lt;/purpose&gt;
      &lt;log&gt;
        &lt;phase endtime="2010-02-08 15:17:47" name="Test" result="PASS"
                score="0" starttime="2010-02-08 15:17:47" type="FAIL"&gt;
          &lt;test message="Checking for the presence of setup rpm"&gt;PASS&lt;/test&gt;
          &lt;test message="File /etc/passwd should exist"&gt;PASS&lt;/test&gt;
          &lt;test message="File '/etc/passwd' should contain 'root'"&gt;PASS&lt;/test&gt;
        &lt;/phase&gt;
      &lt;/log&gt;
    &lt;/BEAKER_TEST&gt;
</code></pre> 

 <i>rlJournalPrintText</i> 

 Print the content of the journal in pretty text format. 

 <pre>
    rlJournalPrintText [--full-journal]
</pre>
<dl>
<dt>--full-journal
<dd> With this option, additional items like some <font SIZE="-1">HW</font> information will be printed in the journal.</dl>
 

 Example: 

 <pre><code>
    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    :: [   LOG    ] :: TEST PROTOCOL
    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    :: [   LOG    ] :: Test run ID   : debugging
    :: [   LOG    ] :: Package       : debugging
    :: [   LOG    ] :: Test started  : 2010-02-08 14:45:57
    :: [   LOG    ] :: Test finished : 2010-02-08 14:45:58
    :: [   LOG    ] :: Test name     :
    :: [   LOG    ] :: Distro:       : Fedora release 12 (Constantine)
    :: [   LOG    ] :: Hostname      : localhost
    :: [   LOG    ] :: Architecture  : i686
    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    :: [   LOG    ] :: Test description
    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    PURPOSE of /examples/beakerlib/Sanity/simple
    Description: Minimal BeakerLib sanity test
    Author: Petr Splichal &lt;psplicha [at] redhat.com&gt;
    This is a minimal sanity test for BeakerLib. It contains a single
    phase with a couple of asserts. We Just check that the "setup"
    package is installed and that there is a sane /etc/passwd file.
    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    :: [   LOG    ] :: Test
    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    :: [   PASS   ] :: Checking for the presence of setup rpm
    :: [   PASS   ] :: File /etc/passwd should exist
    :: [   PASS   ] :: File '/etc/passwd' should contain 'root'
    :: [   LOG    ] :: Duration: 1s
    :: [   LOG    ] :: Assertions: 3 good, 0 bad
    :: [   PASS   ] :: RESULT: Test
</code></pre> 

 <i>rlGetTestState</i> 

 Returns number of failed asserts in so far, 255 if there are more then 255 failures. 

 <pre>
    rlGetTestState
</pre> 

 <i>rlGetPhaseState</i> 

 Returns number of failed asserts in current phase so far, 255 if there are more then 255 failures. 

 <pre>
    rlGetPhaseState
</pre>

<h2>AUTHORS</h2>

<dl>
<dt>&bull;
<dd> Petr Muller &lt;pmuller [at] redhat.com&gt;
<dt>&bull;
<dd> Jan Hutar &lt;jhutar [at] redhat.com&gt;
<dt>&bull;
<dd> Ales Zelinka &lt;azelinka [at] redhat.com&gt;
<dt>&bull;
<dd> Petr Splichal &lt;psplicha [at] redhat.com&gt; 

</dl>

<h2>Index</h2>


