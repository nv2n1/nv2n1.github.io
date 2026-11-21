---

title: "papi_avail(1)"
name: "papi_avail"
section: "1"
letter: "p"
url: "/docs/linux/man/1-papi_avail/"
---

papi_avail - papi_avail utility. 

 file avail.c 

<h2>Name</h2>

 

 papi_avail - provides availability and detail information for PAPI preset events.

<h2>Synopsis</h2>

 

 papi_avail [-adht] [-e event]

<h2>Description</h2>

 

 papi_avail is a PAPI utility program that reports information about the current PAPI installation and supported preset events. Using the -e option, it will also display information about specific native events.

<h2>Options</h2>

 

<dl>
<dt>&bull;
</dt><dd> -a Display only the available PAPI preset events.
</dd><dt>&bull;
</dt><dd> -d Display PAPI preset event information in a more detailed format.
</dd><dt>&bull;
</dt><dd> -h Display help information about this utility.
</dd><dt>&bull;
</dt><dd> -t Display the PAPI preset event information in a tabular format. This is the default.
</dd><dt>&bull;
</dt><dd> -e &lt; event &gt; Display detailed event information for the named event. This event can be either a preset or a native event.</dd></dl>
 

<h2>Bugs</h2>

 

 There are no known bugs in this utility. If you find a bug, it should be reported to the PAPI Mailing List at ptools-perfapi [at] ptools.org.
