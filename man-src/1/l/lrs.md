---
title: "lrs(1)"
name: "lrs"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lrs/"
---

<h2>LRS (Linear Referencing System)</h2>
<p> A Linear Referencing System (LRS) is a system where features (points or segments) are localized by a measure along a linear element. The LRS can be used to reference events for any network of linear features, for example roads, railways, rivers, pipelines, electric and telephone lines, water and sewer networks. An event is defined in LRS by a route ID and a measure. A route is a path on the network, usually composed from more features in the input map. Events can be either points or lines (segments). </p>
<p> LRS is created from input lines and points in vector map. Points &#8211; MP (mileposts) must have attached attributes specifying line and distance. The distances from the beginning of the linear feature in real world are specified by MP+offset. Typically, MP is in kilometers and offset in meters. </p>
<p> The implementation of LRS in GRASS has some particularities.</p>
<h3>Double referenced system</h3>
<p> This feature gives a possibility to continue to use most of old mileposts if only small part of linear object in real world has changed. Example:<br />
 &#8212; road (linear feature) </p>
<p>&nbsp;<wbr>+&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>MP&nbsp;<wbr>(milepost, point, distance from the beginning in km)<br />
 Old situation:<br />
 +&#8212;-+&#8212;-+&#8212;-+&#8212;-+&#8212;-+<br />
 0 2 3 4 5 6<br />
 New situation (for example a new bypass around the village) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>?&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>? </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+&#8212;-+ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>| </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
 +&#8212;-+&#8212;-+ +&#8212;-+&#8212;-+<br />
 0 2 3 4 5 6<br />
 The segment between km 3 and 4 is now longer, it is now 3 km not 1 km as in old version. It would be expensive to change also all MP &gt;= 4, but we cannot use km 4 twice. It is possible to use another notation for the new segment, we reference the segment from the kilometer 3, using only offset. </p>
<p>3+1000&nbsp;<wbr>&nbsp;<wbr>3+2000 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+&#8212;-+ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>| </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|<br />
 +&#8212;-+&#8212;-+ +&#8212;-+&#8212;-+<br />
 0 2 3 3+3000 5 6 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>4<br />
 This way, there is no ambiguity and minimal changes are needed. But the MP 4 is no more the end of segment 3 &#8211; 4 but the end of segment 3+2000 &#8211; 3+3000. This information must be entered to the system and it is done by optional MP attributes:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> end_mp &#8211; end MP</p>
<dt>
<dd> end_off &#8211; end offset</dl>
</dl>
<p> In this case original MP on km 4 will have these attributes:<br />
 start_mp: 4<br />
 start_off: 0<br />
 end_mp: 3<br />
 end_off: 3000<br />
 Because each MP can keep 2 values (start, end) it is called &#8216;double&#8217; referenced LRS. </p>
<p> To avoid potential confusion, MP values are limited to integers only. It would be ambiguous to have for example segments 3.500 &#8211; 3.500+200 and 3.600 &#8211; 3.600+200. The position 3+650 would fall into 2 segments, correct would be 3.600+50. That means, that MP must be the beginning of antonomous segment and all parts which becomes longer then before must be referenced from the last not changed MP. </p>
<p> The MP <i>start_mp</i> and <i>end_mp</i> columns must be decimal, but <i>v.lrs.create</i> takes only the decimal part, and adds its value to offset and prints a warning. </p>
<p> It is highly recommended to work with polylines instead of segmented vector lines. The command <i>v.build.polylines</i> creates this map structure.</p>
<h3>LRS table structure</h3>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| <code>Attribute</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| <code>Type</code><tt>&nbsp;<wbr>&nbsp;<wbr></tt>| <code>Description</code></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| rsid<tt>&nbsp;<wbr>&nbsp;<wbr></tt>| integer<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| reference segment ID, unique in the table</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| lcat<tt>&nbsp;<wbr>&nbsp;<wbr></tt>| integer<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| category of the line in the LRS map</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| lid<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| integer<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| route ID (LID)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| start_map<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| double precision<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| distance measured along the line in LRS map from the beginning of the line to the beginning of the segment (absolute milepost distance)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| end_map<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| double precision<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| distance measured along the line in LRS map from the beginning of the line to the end of the segment (absolute distance of subsequent milepost)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| start_mp<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| double precision<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| milepost number assigned to the start of the segment</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| start_off<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| double precision<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| distance from start_mp to the start of the segment measured along the physical object</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| end_mp<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| double precision<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| milepost number assigned to the end of the segment</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| end_off<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| double precision<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| distance from end_mp to end of the segment measured along the physical object</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| end_type<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| integer<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>| 1: the same as specified for from_ ; 2: calculated from map along the line from previous MP; 3: defined by user </p>
<h3>Available commands</h3>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> v.lrs.create to create a linear referencing system,</p>
<dt>
<dd> v.lrs.label to create stationing on the LRS,</p>
<dt>
<dd> v.lrs.segment to create points/segments on LRS, and</p>
<dt>
<dd> v.lrs.where to find line id and real km+offset for given points in vector map using linear referencing system.</dl>
</dl>
<h3>Input lines for v.lrs.segment and v.lrs.label</h3>
<p> <i>v.lrs.create</i> joins all connected lines of the same line ID into one line, the LRS library and other modules using LRS expect this! LR_get_nearest_offset in the LRS library checks duplicate segments only by line_cat and map_offset, not by coordinates in map.</p>
<h3>Duplicate positions</h3>
<p> It can happen that one offset appears on 2 different lines:<br />
 &#8212;&#8212;1&#8212;&#8212;- &#8212;&#8212;&#8211;2&#8212;&#8212;<br />
 +0.0 +1.0 +2.0<br />
 In this case, the module gives error because the position results in 2 points. </p>
<p> It can be also intended, for example a part of the road is shared with another one, but MP are used only for one: </p>
<p>&nbsp;<wbr>+&nbsp;<wbr>road1/km15&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+&nbsp;<wbr>road1/km22 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>rs&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/ </p>
<p>rs road1/km17&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/&nbsp;<wbr>road1/km20 </p>
<p>&nbsp;<wbr>+&#8212;&#8212;&#8212;&#8212;&#8211;+&nbsp;<wbr> </p>
<p>/&nbsp;<wbr>road2/km52&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rs road2/km52 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>/&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rs </p>
<p>&nbsp;<wbr>+&nbsp;<wbr>road2/km50&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+&nbsp;<wbr>road2/km54&nbsp;<wbr> </p>
<h2>NOTES</h2>
<p> Explanations of selected options:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> llayer: vector layer in line map (usually 1; see vectorintro for &quot;layer&quot; concept)</p>
<dt>
<dd> player: vector layer in point map (usually 1; see vectorintro for &quot;layer&quot; concept)</p>
<dt>
<dd> rsdriver: Driver name for LRS table &#8211; DBMI SQL driver (dbf, pg, mysql, sqlite, etc)</p>
<dt>
<dd> rsdatabase: Database name for LRS table &#8211; DBMI SQL database name (e.g., &quot;lrsdb&quot;)</p>
<dt>
<dd> rstable: Name of the LRS table &#8211; DBMI SQL table name (e.g., &quot;streamslrs&quot;)</dl>
</dl>
<h2>SEE ALSO</h2>
<p> <i>R. Blazek, 2004, Introducing the Linear Reference System in GRASS, Bangkok, GRASS User Conf. Proc.</i><br />
 <i>R. Blazek, 2005, Introducing the Linear Reference System in GRASS, International Journal of Geoinformatics, Vol. <a href="/docs/linux/man/3-1/">1</a>(3), pp. 95-100</i> </p>
<p> <i>v.build.polylines</i>, <i>v.lrs.create</i>, <i>v.lrs.segment</i>, <i>v.lrs.where</i>, <i>v.lrs.label</i></p>
<h2>AUTHOR</h2>
<p> Radim Blazek, ITC-irst/MPA Solutions Trento<br />
 Documentation update (based on above journal article and available fragments): Markus Neteler </p>
<p> <i>Last changed: $Date: 2007-12-17 14:45:01 +0100 (Mon, 17 Dec 2007) $</i> </p>
<h2>Index</h2>
