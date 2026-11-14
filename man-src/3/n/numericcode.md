---
title: "numericcode(3)"
name: "numericcode"
section: "3"
letter: "n"
url: "/docs/linux/man/3-numericcode/"
description: "QuantLib::Currency – Currency specification"
---

<p>QuantLib::Currency &#8211; Currency specification </p>
<h2>Synopsis</h2>
<pre><code>const std::string &amp; name () const


currency name, e.g, 'U.S. Dollar'


const std::string &amp; code () const


ISO 4217 three-letter code, e.g, 'USD'.


Integer numericCode () const


ISO 4217 numeric code, e.g, '840'.


const std::string &amp; symbol () const


symbol, e.g, '$'


const std::string &amp; fractionSymbol () const


fraction symbol, e.g, '¢'


Integer fractionsPerUnit () const


number of fractionary parts in a unit, e.g, 100


const Rounding &amp; rounding () const


rounding convention


std::string format () const


output format</code></pre>
<p> Inherited by <code>ARSCurrency</code>, <code>ATSCurrency</code>, <code>AUDCurrency</code>, <code>BDTCurrency</code>, <code>BEFCurrency</code>, <code>BGLCurrency</code>, <code>BRLCurrency</code>, <code>BYRCurrency</code>, <code>CADCurrency</code>, <code>CHFCurrency</code>, <code>CLPCurrency</code>, <code>CNYCurrency</code>, <code>COPCurrency</code>, <code>CYPCurrency</code>, <code>CZKCurrency</code>, <code>DEMCurrency</code>, <code>DKKCurrency</code>, <code>EEKCurrency</code>, <code>ESPCurrency</code>, <code>EURCurrency</code>, <code>FIMCurrency</code>, <code>FRFCurrency</code>, <code>GBPCurrency</code>, <code>GRDCurrency</code>, <code>HKDCurrency</code>, <code>HUFCurrency</code>, <code>IEPCurrency</code>, <code>ILSCurrency</code>, <code>INRCurrency</code>, <code>IQDCurrency</code>, <code>IRRCurrency</code>, <code>ISKCurrency</code>, <code>ITLCurrency</code>, <code>JPYCurrency</code>, <code>KRWCurrency</code>, <code>KWDCurrency</code>, <code>LTLCurrency</code>, <code>LUFCurrency</code>, <code>LVLCurrency</code>, <code>MTLCurrency</code>, <code>MXNCurrency</code>, <code>NLGCurrency</code>, <code>NOKCurrency</code>, <code>NPRCurrency</code>, <code>NZDCurrency</code>, <code>PEHCurrency</code>, <code>PEICurrency</code>, <code>PENCurrency</code>, <code>PKRCurrency</code>, <code>PLNCurrency</code>, <code>PTECurrency</code>, <code>ROLCurrency</code>, <code>RONCurrency</code>, <code>SARCurrency</code>, <code>SEKCurrency</code>, <code>SGDCurrency</code>, <code>SITCurrency</code>, <code>SKKCurrency</code>, <code>THBCurrency</code>, <code>TRLCurrency</code>, <code>TRYCurrency</code>, <code>TTDCurrency</code>, <code>TWDCurrency</code>, <code>USDCurrency</code>, <code>VEBCurrency</code>, and <code>ZARCurrency</code>.</p>
<h3>Public Member Functions</h3>
<p><code>Currency</code> ()<br />
 <i>default constructor </i> <code>Inspectors</code> </p>
<pre><code>const std::string &amp; name () const


currency name, e.g, 'U.S. Dollar'


const std::string &amp; code () const


ISO 4217 three-letter code, e.g, 'USD'.


Integer numericCode () const


ISO 4217 numeric code, e.g, '840'.


const std::string &amp; symbol () const


symbol, e.g, '$'


const std::string &amp; fractionSymbol () const


fraction symbol, e.g, '¢'


Integer fractionsPerUnit () const


number of fractionary parts in a unit, e.g, 100


const Rounding &amp; rounding () const


rounding convention


std::string format () const


output format</code></pre>
<p> <code>Other information</code> </p>
<p> bool <code>empty</code> () const<br />
 <i>is this a usable instance? </i><br />
 const <code>Currency</code> &amp; <code>triangulationCurrency</code> () const<br />
 <i>currency used for triangulated exchange when required </i></p>
<h3>Protected Attributes</h3>
<p>boost::shared_ptr&lt; Data &gt; <code>data_</code></p>
<h3>Related Functions</h3>
<p>(Note that these are not member functions.)<br />
 bool <code>operator==</code> (const <code>Currency</code> &amp;, const <code>Currency</code> &amp;) </p>
<p> bool <code>operator!=</code> (const <code>Currency</code> &amp;, const <code>Currency</code> &amp;) </p>
<p> std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;, const <code>Currency</code> &amp;)</p>
<h2>Detailed Description</h2>
<p>Currency specification</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3><code>Currency</code> ()</h3>
<p>default constructor </p>
<p> Instances built via this constructor have undefined behavior. Such instances can only act as placeholders and must be reassigned to a valid currency before being used.</p>
<h2>Member Function Documentation</h2>
<h3>std::string format () const</h3>
<p>output format </p>
<p> The format will be fed three positional parameters, namely, value, code, and symbol, in this order.</p>
<h2>Friends And Related Function Documentation</h2>
<h3>bool operator== (const <code>Currency</code> &amp;, const <code>Currency</code> &amp;) [related]</h3>
<h3>bool operator!= (const <code>Currency</code> &amp;, const <code>Currency</code> &amp;) [related]</h3>
<h3>std::ostream &amp; operator&lt;&lt; (std::ostream &amp;, const <code>Currency</code> &amp;) [related]</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
