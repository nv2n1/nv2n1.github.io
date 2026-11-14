---
title: "opaxlattopology(8)"
name: "opaxlattopology"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opaxlattopology/"
description: "opaxlattopology Generates a topology XML file of a cluster using topology.csv, linksum_swd06.csv, and linksum_swd24.csv as input. The topology file can be used to bring up and verify the cluster. N..."
---

<p>opaxlattopology Generates a topology XML file of a cluster using topology.csv, linksum_swd06.csv, and linksum_swd24.csv as input. The topology file can be used to bring up and verify the cluster. <code>NOTE:</code> The topology.csv input file must be present in the same directory from which the script operates, but the linksum CSV files are read from the /usr/lib/opa-ff/samples directory. </p>
<h2>Syntax</h2>
<p>opaxlattopology [-d <i>level</i>-v <i>level</i>-i <i>level</i>-c <i>char</i>-K -?]<br />
 [source [dest]]</p>
<h2>Options</h2>
<dl>
<dt>-d <i>level</i></p>
<dd>Output detail level. Default = 0. Levels are additive. </p>
<dd>By default, the top level is always produced. Switch, rack, and rack group topology files can be added to the output by choosing the appropriate level. If the output at the group or rack level is specified, then group or rack names must be provided in the spreadsheet. Detailed output can be specified in any combination. A directory for each topology XML file is created hierarchically, with group directories (if specified) at the highest level, followed by rack and switch directories (if specified).</p>
<dl>
<dd>
<dl>
<dd>1 Intel(R) Omni-Path Edge Switch 100 Series topology files. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>2 Rack topology files. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>4 Rack group topology files. </p>
</dl>
</dl>
<dt>-v <i>level</i></p>
<dd>Verbose level. Range = 0 &#8211; 8. Default = 2. </p>
<dl>
<dd>
<dl>
<dd>0 No output. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>1 Progress output. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>2 Reserved. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>4 Time stamps. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>8 Reserved. </p>
</dl>
</dl>
<dt>-i <i>level</i></p>
<dd>Output indent level. Range = 0 &#8211; 15. Default = 0. </p>
<dt>-c <i>char</i></p>
<dd>NodeDesc concatenation character. Used when creating NodeDesc values (that is, Name to Name-2, Name to HFI-1, and so on). A space is used by default, but another character, such as underscore, can be specified. </p>
<dt>-K</p>
<dd>Does not clean temporary files. Prevents temporary files in each topology directory from being removed. Temporary files contain CSV formatted lists of links, HFIs, and switches used to create a topology XML file. Temporary files are not typically needed after a topology file is created, however they are used for creating linksum_swd06.csv and linksum_swd24.csv files, or can be retained for subsequent inspection or processing. </p>
<dt>-?</p>
<dd>Prints this output. </p>
</dl>
<h2>Description</h2>
<p>The opaxlattopology script reads the topology.csv file from the local directory, and reads the other files from /usr/lib/opa-ff/samples/linksum_swd06.csv and /usr/lib/opa-ff/samples/linksum_swd24.csv. The topology.csv file is created from the topology.xlsx spreadsheet by saving the Fabric Links tab as a .CSV file to topology.csv. A sample topology.xlsx is located in the /usr/lib/opa-ff/samples/ directory. Inspect the topology.csv file to ensure that each row contains the correct and same number of comma separators. Any extraneous entries in the spreadsheet can cause the CSV output to have extra fields. </p>
<p> The script outputs one or more topology files starting with topology.0:0.xml. The topology.csv input file must be present in the same directory from which the script operates, but the linksum CSV files are read from the /usr/lib/opa-ff/samples directory.</p>
<h2>Example</h2>
<p>opaxlattopology<br />
 # reads default input &#8216;topology.csv&#8217; and creates default<br />
 # output &#8216;topology.0:0.xml&#8217; </p>
<p> opaxlattopology fabric_2.csv<br />
 # reads input &#8216;fabric_2.csv&#8217; and creates default output </p>
<p> See topology.xlsx for examples of links between HFI and Edge SW (rows 4-7), HFI and Core SW (rows 8-11), and Edge SW and Core SW (rows 12-15).</p>
<h2>Environment Variables</h2>
<p>The following environment variables allow user-specified MTU.</p>
<dl>
<dt><code>MTU_SW_SW</code></p>
<dd>If set, it overrides default MTU on switch-to-switch links. Default = 10240 </p>
<dt><code>MTU_SW_HFI</code></p>
<dd>If set, it overrides default MTU on switch-to-HFI links. Default = 8192 </p>
</dl>
<h2>Creating linksum Files</h2>
<p>The linksum_swd06.csv and linksum_swd24.csv files are provided as stand-alone files in the /usr/lib/opa-ff/samples directory. However, they can be recreated (or modified) from the spreadsheet, if needed, by performing the following steps: </p>
<dl>
<dt>1)</p>
<dd>Save each of the following from the topology.xlsx file as individual .csv files:</p>
<dt>&bull;</p>
<dd>Internal SWD06 Links tab as linksum_swd06.csv</p>
<dt>&bull;</p>
<dd>Internal SWD24 Links tab as linksum_swd24.csv</p>
<dt>&bull;</p>
<dd>Fabric Links tab as topology.csv </p>
<dt>2)</p>
<dd>For each saved topology.csv file, run the script with the -K option. </p>
<dt>3)</p>
<dd>Upon completion of the script, save the top level linksum.csv file as linksum_swd06.csv or linksum_swd24.csv as appropriate. </p>
</dl>
<h2>Including SM Blocks in Topology</h2>
<p>You must manually edit the /etc/sysconfig/opa/topology.0:0.xml file to include SM blocks for each SM in your fabric. opaxlattopology translates the topology.csv file which does not include SM blocks in the xml file by default. If manual edits are not completed, then the command opareport -o verifyall -T topology.0:0.xml fails with errors similar to the following:# opareport -o verifyall -T topology.0:0.xml<br />
 SMs Topology Verification </p>
<p> SMs Found with incorrect configuration:<br />
 NodeGUID Port PortGUID Type Name<br />
 0x0011750101671ed9 1 0x0011750101671ed9 FI phkp3un86 hfi1_0<br />
 NodeDetails: koplab<br />
 Unexpected SM </p>
<p> 1 of 1 Fabric SMs Checked </p>
<p> SMs Expected but Missing or Duplicate in input:<br />
 0 of 0 Input SMs Checked </p>
<p> Total of 1 Incorrect SMs found<br />
 0 Missing, 1 Unexpected, 0 Duplicate, 0 Different </p>
<p> To retrieve the info for the SM block, use the command opareport -o nodes -F sm as shown in the following example.<br />
 # opareport -o nodes -F sm<br />
 Getting All Node Records&#8230;<br />
 Done Getting All Node Records<br />
 Done Getting All Link Records<br />
 Done Getting All Cable Info Records<br />
 Done Getting All SM Info Records<br />
 Node Type Summary<br />
 Focused on:<br />
 Port: 1 0x0011750101671ed9<br />
 in Node: 0x0011750101671ed9 FI phkp3un86 hfi1_0 </p>
<p> 3 Connected FIs in Fabric:<br />
 Name: phkp3un86 hfi1_0<br />
 NodeGUID: 0x0011750101671ed9 Type: FI<br />
 Ports: 1 PartitionCap: 16 SystemImageGuid: 0x0011750101671ed9<br />
 BaseVer: 128 SmaVer: 128 VendorID: 0x1175 DeviceID: 0x24f0 Rev: 0x10<br />
 1 Connected Ports:<br />
 PortNum: 1 LID: 0x0001 GUID: 0x0011750101671ed9<br />
 Neighbor: Name: phedfim20<br />
 NodeGUID: 0x0011750102648205 Type: SW PortNum: 46<br />
 Width: 4 Speed: 25Gb Downgraded? No<br />
 1 Matching FIs Found </p>
<p> 1 Connected Switches in Fabric:<br />
 0 Matching Switches Found </p>
<p> 1 Connected SMs in Fabric:<br />
 State: Master Name: phkp3un86 hfi1_0<br />
 NodeGUID: 0x0011750101671ed9 Type: FI<br />
 PortNum: 1 LID: 0x0001 PortGUID: 0x0011750101671ed9<br />
 SM_Key: 0x0000000000000000 Priority: 0 ActCount: 0x0000bcb2<br />
 1 Matching SMs Found</p>
