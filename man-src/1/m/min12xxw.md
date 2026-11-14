---
title: "min12xxw(1)"
name: "min12xxw"
section: "1"
letter: "m"
url: "/docs/linux/man/1-min12xxw/"
description: "min12xxw – Convert pbmraw streams to Minolta PagePro 12xxW languages"
---

<h2 class="name">NAME</h2>
<p> min12xxw &#8211; Convert pbmraw streams to Minolta PagePro 12xxW languages </p>
<h2>SYNOPSIS</h2>
<p> min12xxw [options] </p>
<h2>DESCRIPTION</h2>
<p> <code>Min12xxw</code> is a filter which converts pbmraw streams (produced by ghostscript, for example) to the printer language of Minolta PagePro 1[234]xxW printers. </p>
<h2>COMMAND-LINE OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Gives usage information (help) </p>
<dt><code>-v, &#8211;version</code></p>
<dd> Displays the version number and exit </p>
<dt><code>-e, &#8211;ecomode</code></p>
<dd> Enables economic mode which saves toner by leaving every other scanline blank. This degrades the printout&#8217;s resolution a little, the effect is most easily seen (and looks particularly bad) when printing in 300 dpi mode. </p>
<dt><code>-s, &#8211;status</code></p>
<dd> Query the printer status, page counter and whatever information can be retrieved. The printer status is basically an unprocessed dump of what the printer sends, so unexpected things may happen if the printer sends funny data because it got confused somehow&#8230; This might however still be useful. The page counter and other information is heavily processed and should be more reliable. Note that for queries to be made, the printer must (of course) be switched on, with all cables connected, and not be busy printing (or your print job may be truncated). See the <code>-d</code> option below which sets the device file to use. This has so far only been tested on 1200W, 1350W and 1400W printers. Send mail if it works for others as well. </p>
<dt><code>-d dev, &#8211;device dev</code></p>
<dd> Sets the device file to use for queries. The default is /dev/lp0. </p>
<p> Please note that this option is only meaningful with the &quot;-s&quot; or &quot;&#8211;status&quot; option. If you intend to send a document to the printer, you have to redirect min12xxw&#8217;s standard output to the device file in question. See the documentation that came with your shell on how to do that. </p>
<dt><code>-n, &#8211;nomargins</code></p>
<dd> Disables the enforcement of the 0.17 inch margins on all sides of the paper. The converter discards the equivalent of this length of its input because ghostscript outputs a full page with margins. If you arranged in some way for the input to be marginless, or have slightly larger paper, you can give this option to include the full input with margins. Please note that for very small page dimensions, min12xxw might need to disable enforcing the page margins for all pages following the offending page to make the job printable. In that case, a warning message will be printed on the standard error stream to inform the user. </p>
<dt><code>-m model, &#8211;model model</code></p>
<dd> Sets which printer model to produce output for. Currently, no checks for features only available to specific models are made (available paper trays differ from model to model, for example). Let me know if this causes problems. Available models are: 1200W, 1250W, 1300W, 1350W, 1400W. 1200W is the default. As an alternative, you can also symlink, link or rename your executable to min1200w, min1250w, min1300w, min1350w or min1400w, thus making the model specified in the filename the default model. This saves you from typing the model selection option again and again and again&#8230; Please note that you <code>must</code> supply the model option correctly if you drive any other model than what is the default. If you fail to do so, your printer will not produce any output or react to status queries from the host. </p>
<dt><code>-r resolution, &#8211;res resolution</code></p>
<dd> Sets the resolution to either 300, 600 or 1200 dpi (600 dpi is the default). Keep in mind that you need to produce your output accordingly. It is also possible to specify the resolution as (horizontal)x(vertical) resolution (e.g. -r 1200&#215;600) where horizontal resolution may be once or twice the vertical resolution. The maximum resolution is 1200 dpi in both vertical and horizontal direction. The minimum vertical resolution for mixed resolution printing seems to be 600 dpi. 300 dpi printing has only been tested on 1200W, 1350W and 1400W models. Mixed resolution printing was seen for 13xxW and 1400W models only, but tests show that the 1200W is capable of handling it as well, so chances are that 1250W printers won&#8217;t have trouble, either. </p>
<dt><code>-t tray, &#8211;tray tray</code></p>
<dd> Sets the paper tray to be used. Valid values for tray are &quot;auto&quot;, &quot;tray1&quot;, &quot;tray2&quot; and &quot;manual&quot;, with &quot;auto&quot; being the default. Not all printer models have all sorts of paper trays. &quot;auto&quot; should be safe on all of them, I think. In fact, the PagePro 1400W seems to have only this kind of paper tray. </p>
<dt><code>-p type, &#8211;papertype type</code></p>
<dd> Sets the type of paper used. Type can be one of &quot;normal&quot;, &quot;thick&quot;, &quot;transparency&quot;, &quot;envelope&quot; or &quot;postcard&quot;. &quot;normal&quot; is the default. </p>
<dt><code>-f fmt, &#8211;paperformat fmt</code></p>
<dd> This sets the paper format to be used for the print job. The default value for fmt is &quot;a4&quot;. Valid values are given below. </p>
<dt><code>a4</code></p>
<dd> A4 paper (210 mm x 297 mm) </p>
<dt><code>b5</code></p>
<dd> B5 envelope (176 mm x 250 mm) </p>
<dt><code>a5</code></p>
<dd> A5 paper (148 mm x 210 mm) </p>
<dt><code>jpost</code></p>
<dd> Post card (100 mm x 148 mm) </p>
<dt><code>corpost</code></p>
<dd> Correspondence Postcard (148 mm x 200 mm) </p>
<dt><code>jisy6</code></p>
<dd> JIS Yokei 6-gou paper (98 mm x 190 mm) </p>
<dt><code>jisy0</code></p>
<dd> JIS Yokei 0-gou paper (120 mm x 235 mm) </p>
<dt><code>chinese16k</code></p>
<dd> Chinese 16K paper (185 mm x 260 mm) </p>
<dt><code>chinese32k</code></p>
<dd> Chinese 32K paper (130 mm x 185 mm) </p>
<dt><code>legal</code></p>
<dd> Legal paper (8.5&quot; x 14&quot;) </p>
<dt><code>glegal</code></p>
<dd> G. Legal paper (8.5&quot; x 13&quot;) </p>
<dt><code>letter</code></p>
<dd> Letter paper (8.5&quot; x 11&quot;) </p>
<dt><code>gletter</code></p>
<dd> G. Letter paper (8.5&quot; x 10.5&quot;) </p>
<dt><code>executive</code></p>
<dd> Executive paper (7.25&quot; x 10.5&quot;) </p>
<dt><code>halfletter</code></p>
<dd> Halfletter paper (5.5&quot; x 8.5&quot;) </p>
<dt><code>envmonarch</code></p>
<dd> Envelope Monarch (3.875&quot; x 7.5&quot;) </p>
<dt><code>env10</code></p>
<dd> Envelope COM-10 (8.125&quot; x 9.5&quot;) </p>
<dt><code>envdl</code></p>
<dd> Envelope DL (110 mm x 220 mm) </p>
<dt><code>envc5</code></p>
<dd> Envelope C5 (162 mm x 229 mm) </p>
<dt><code>envc6</code></p>
<dd> Envelope C6 (114 mm x 162 mm) </p>
<dt><code>envb5</code></p>
<dd> Envelope B5 (176 mm x 250 mm) </p>
<dt><code>Choukei-3Gou</code></p>
<dd> Choukei-3Gou paper (120mm x 235 mm) </p>
<dt><code>Choukei-4Gou</code></p>
<dd> Choukei-4Gou paper (90 mm x 205 mm) </p>
<dt><code>custom</code></p>
<dd> Custom paper size </p>
<dt><code>envb6</code></p>
<dd> Envelope 6 3/4 (3.625&quot; x 6.5&quot;) </p>
<dt><code>folio</code></p>
<dd> F4/Folio paper (210 mm x 330 mm) </p>
<dt><code>jisy1</code></p>
<dd> JIS Yokei 1-gou (120 mm x 176 mm) </p>
<dt><code>jisy2</code></p>
<dd> JIS Yokei 2-gou (105 mm x 235 mm) </p>
<dt><code>quadpost</code></p>
<dd> Quad postcard (200 mm x 296 mm) </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>gs -q -dBATCH -dSAFER -dQUIET -dNOPAUSE -sPAPERSIZE=a4 -r1200 -sDEVICE=pbmraw -sOutputFile=- &#8211; &lt; test.ps | min12xxw -r 1200 &gt; test.min</code></p>
<dd> This would convert a postscript file test.ps to a file test.min which could be sent directly to the printer, a 1200W to be exact. The output is rendered at 1200 dpi. If you have to drive some other model, see the model selection option (-m) above. </p>
</dl>
<h2>PORTABILITY</h2>
<p> <code>Min12xxw</code> should run on most *nix-like workstations without major problems. Library functions which are known to be missing on non-Linux systems such as getline or getopt_long may have to be replaced by an appropriate substitute. In case of getline and getopt_long this has already been done. The query options may or may not work on other systems, depending on the characteristics of the printer driver and the interface used (USB, very old style parallel port or a more recent one&#8230;). </p>
<h2>BUGS/LIMITATIONS/CONTRIBUTORS</h2>
<p> <code>Min12xxw</code> was written without any documentation from the manufacturer. The description of the printer language may be inaccurate or even wrong because it was obtained by looking at the output of the windoof driver only. The code dealing with the compression of raster data is in its spirit heavily based on an initial driver by Adam Bocim &lt;beetman [at] seznam.cz&gt; who managed to find out how things are done (thanks, Adam, you did a great job!). This new version is considerably faster, implemented more cleanly and (hopefully) well documented. </p>
<p> It also features querying the printer status and page counter, a suggestion made by Bruno Schoedlbauer &lt;bruno.schoedlbauer [at] gmx.de&gt;, who also pointed me to a nice USB sniffer by Benoit Papillault for Windoof 98 and up, see <a rel="nofollow" href="http://benoit.papillault.free.fr/usbsnoop.">http://benoit.papillault.free.fr/usbsnoop.</a> (That little program may prove very helpful on similar occasions. Happy USB sniffing&#8230;) </p>
<p> David Hamilton &lt;dhamilto [at] angel.homeip.net&gt; has helped a lot in testing and developing the support for the PagePro 1350W. </p>
<p> Even though this program has been designed with care and much thought, no-one can guarantee that this program will not damage your printer, computer or even your neighbour&#8217;s car, because it was built without knowing exactly how things work, it&#8217;s only a (hopefully) reasonable guess. (However, my printer does still work, even after the testing phase when a lot of wrong stuff was sent to it. And my neighbour hasn&#8217;t complained either&#8230;) </p>
<p> Most of the available paper sizes have not actually been verified to work as advertised &#8211; reports about successes or problems are welcome. Also the code for querying the printer is not heavily tested. If you have comments to make or know more about the format than I do, please share your thoughts and your knowledge. </p>
<p> 13xxW series support seems to be relatively well tested by now. Send mail with feedback if you have such a printer and you experience problems. </p>
<p> 1400W support is pretty new &#8211; please send e-mail if it works or if you run into problems. Feedback on models for which support has just been completed is very important to improve and stabilise this support. </p>
<p> Bugs and problems reports are generally welcome because I just don&#8217;t have the time to test everything out. I needed a filter and here it is. If it does not work &#8211; complain ;-) </p>
<h2>AUTHOR</h2>
<p> <code>Min12xxw</code> was written by Manuel Tobias Schiller (mala [at] hinterbergen.de). </p>
<h2>Index</h2>
