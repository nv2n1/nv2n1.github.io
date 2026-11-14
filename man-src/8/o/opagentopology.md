---
title: "opagentopology(8)"
name: "opagentopology"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opagentopology/"
description: "opagentopology Generates sample topology verification XML. Provides an example of using opaxmlgenerate and is a prototype for customization. Uses CSV input files opatopology_links.txt, opatopology_..."
---

<p>opagentopology Generates sample topology verification XML. Provides an example of using opaxmlgenerate and is a prototype for customization. Uses CSV input files opatopology_links.txt, opatopology_FIs.txt, and opatopology_SWs.txt to generate LinkSummary, Node FIs, and Node SWs information respectively. These files are samples of what might be produced as part of translating a user custom file format into temporary intermediate CSV files. LinkSummary information includes Link, Cable, and Port information. Note that opagentopology (not opaxmlgenerate) generates the XML version string as well as the #8217lt;Topology&gt; and &lt;LinkSummary&gt; lines. Also note that the indent level is at the default value of zero (0). The portions of the script that call opaxmlgenerate follow:<br />
 opaxmlgenerate -X /usr/lib/opa-ff/samples/opatopology_1.txt -d ; -h Link -g Rate -g<br />
 Rate_Int -g MTU -g LinkDetails -h Cable -g CableLength -g CableLabel -g<br />
 CableDetails -e Cable -h Port -g NodeGUID -g PortNum -g NodeDesc -g PortGUID -g<br />
 NodeType -g NodeType_Int -g PortDetails -e Port -h Port -g NodeGUID -g PortNum -g<br />
 NodeDesc -g PortGUID -g NodeType -g NodeType_Int -g PortDetails -e Port -e Link </p>
<p> opaxmlgenerate -X /usr/lib/opa-ff/samples/opatopology_2.txt -d ; -h Node -g NodeGUID -g<br />
 NodeDesc -g NodeDetails -g HostName -g NodeType -g NodeType_Int -g NumPorts -e Node </p>
<h2>opatopology_links.txt</h2>
<p>This file can be found in /usr/lib/opa-ff/samples/ . For brevity, this sample shows only two links. The second link shows an example of omitting some information. In the second line, the MTU, LinkDetails, and other fields are not present, which is indicated by an empty value for the field (no entry between the semicolon delimiters). </p>
<p> <code>NOTE:</code> The following example exceeds the available width of the page. For readability, a blank line is shown between lines to make it clear where the line ends. In an actual link file, no blank lines are used. </p>
<p> 25g;2048;0;IO Server Link;11m;S4567;cable model 456;0x0002c9020020e004;1;bender HFI-1;0x0002c9020020e004;FI;Some info about port;0x0011750007000df6;7;Switch 1234 Leaf 4;;SW;<br />
 25g;;0;;;;;0x0002c9020025a678;1;mindy2 HFI-1;;FI;;0x0011750007000e6d;4;Switch 2345 Leaf 5;;SW;</p>
<h2>opatopology_FIs.txt</h2>
<p>This file can be found in /usr/lib/opa-ff/samples/ . For brevity, this sample shows only two nodes. </p>
<p> 0x0002c9020020e004;bender HFI-1;More details about node<br />
 0x0002c9020025a678;mindy2 HFI-1;Node details</p>
<h2>opatopology_SWs.txt</h2>
<p>This file can be found in /usr/lib/opa-ff/samples/ . For brevity, this sample shows only two nodes. </p>
<p> 0x0011750007000df6;Switch 1234 Leaf 4; 0x0011750007000e6d;Switch 2345 Leaf 5;</p>
<h2>opatopology_SMs.txt</h2>
<p>This file can be found in /usr/lib/opa-ff/samples/ . For brevity, this sample shows only one node. </p>
<p> 0x0002c9020025a678;1;mindy2 HFI-1;0x0011750007000e6d;FI;details about SM</p>
<h2>Example</h2>
<p>When run against the supplied topology input files, opagentopology produces: </p>
<pre><code>#8217lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot; ?&gt;

#8217lt;Topology&gt;

#8217lt;LinkSummary&gt;

#8217lt;Link&gt;

#8217lt;Rate&gt;25g&lt;/Rate&gt;

#8217lt;MTU&gt;2048&lt;/MTU&gt;

#8217lt;Internal&gt;0&lt;/Internal&gt;

#8217lt;LinkDetails&gt;IO Server Link&lt;/LinkDetails&gt;

#8217lt;Cable&gt;

#8217lt;CableLength&gt;11m&lt;/CableLength&gt;

#8217lt;CableLabel&gt;S4567&lt;/CableLabel&gt;

#8217lt;CableDetails&gt;cable model 456&lt;/CableDetails&gt;

#8217lt;/Cable&gt;

#8217lt;Port&gt;

#8217lt;NodeGUID&gt;0x0002c9020020e004&lt;/NodeGUID&gt;

#8217lt;PortNum&gt;1&lt;/PortNum&gt;

#8217lt;NodeDesc&gt;bender HFI-1&lt;/NodeDesc&gt;

#8217lt;PortGUID&gt;0x0002c9020020e004&lt;/PortGUID&gt;

#8217lt;NodeType&gt;FI&lt;/NodeType&gt;

#8217lt;PortDetails&gt;Some info about port&lt;/PortDetails&gt;

#8217lt;/Port&gt;

#8217lt;Port&gt;

#8217lt;NodeGUID&gt;0x0011750007000df6&lt;/NodeGUID&gt;

#8217lt;PortNum&gt;7&lt;/PortNum&gt;

#8217lt;NodeDesc&gt;Switch 1234 Leaf 4&lt;/NodeDesc&gt;

#8217lt;NodeType&gt;SW&lt;/NodeType&gt;

#8217lt;/Port&gt;

#8217lt;/Link&gt;

#8217lt;Link&gt;

#8217lt;Rate&gt;25g&lt;/Rate&gt;

#8217lt;Internal&gt;0&lt;/Internal&gt;

#8217lt;Cable&gt;

#8217lt;/Cable&gt;

#8217lt;Port&gt;

#8217lt;NodeGUID&gt;0x0002c9020025a678&lt;/NodeGUID&gt;

#8217lt;PortNum&gt;1&lt;/PortNum&gt;

#8217lt;NodeDesc&gt;mindy2 HFI-1&lt;/NodeDesc&gt;

#8217lt;NodeType&gt;FI&lt;/NodeType&gt;

#8217lt;/Port&gt;

#8217lt;Port&gt;

#8217lt;NodeGUID&gt;0x0011750007000e6d&lt;/NodeGUID&gt;

#8217lt;PortNum&gt;4&lt;/PortNum&gt;

#8217lt;NodeDesc&gt;Switch 2345 Leaf 5&lt;/NodeDesc&gt;

#8217lt;NodeType&gt;SW&lt;/NodeType&gt;

#8217lt;/Port&gt;

#8217lt;/Link&gt;

#8217lt;/LinkSummary&gt;

#8217lt;Nodes&gt;

#8217lt;FIs&gt;

#8217lt;Node&gt;

#8217lt;NodeGUID&gt;0x0002c9020020e004&lt;/NodeGUID&gt;

#8217lt;NodeDesc&gt;bender HFI-1&lt;/NodeDesc&gt;

#8217lt;NodeDetails&gt;More details about node&lt;/NodeDetails&gt;

#8217lt;/Node&gt;

#8217lt;Node&gt;

#8217lt;NodeGUID&gt;0x0002c9020025a678&lt;/NodeGUID&gt;

#8217lt;NodeDesc&gt;mindy2 HFI-1&lt;/NodeDesc&gt;

#8217lt;NodeDetails&gt;Node details&lt;/NodeDetails&gt;

#8217lt;/Node&gt;

#8217lt;/FIs&gt;

#8217lt;Switches&gt;

#8217lt;Node&gt;

#8217lt;NodeGUID&gt;0x0011750007000df6&lt;/NodeGUID&gt;

#8217lt;NodeDesc&gt;Switch 1234 Leaf 4&lt;/NodeDesc&gt;

#8217lt;/Node&gt;

#8217lt;Node&gt;

#8217lt;NodeGUID&gt;0x0011750007000e6d&lt;/NodeGUID&gt;

#8217lt;NodeDesc&gt;Switch 2345 Leaf 5&lt;/NodeDesc&gt;

#8217lt;/Node&gt;

#8217lt;/Switches&gt;

#8217lt;SMs&gt;

#8217lt;SM&gt;

#8217lt;NodeGUID&gt;0x0002c9020025a678&lt;/NodeGUID&gt;

#8217lt;PortNum&gt;1&lt;/PortNum&gt;

#8217lt;NodeDesc&gt;mindy2 HFI-1&lt;/NodeDesc&gt;

#8217lt;PortGUID&gt;0x0011750007000e6d&lt;/PortGUID&gt;

#8217lt;NodeType&gt;FI&lt;/NodeType&gt;

#8217lt;SMDetails&gt;details about SM&lt;/SMDetails&gt;

#8217lt;/SM&gt;

#8217lt;/SMs&gt;

#8217lt;/Nodes&gt;

#8217lt;/Topology&gt;

</code></pre>
