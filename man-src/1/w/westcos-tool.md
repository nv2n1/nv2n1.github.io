---
title: "westcos-tool(1)"
name: "westcos-tool"
section: "1"
letter: "w"
url: "/docs/linux/man/1-westcos-tool/"
description: "westcos-tool – utility for manipulating data structure on westcos smart card and similar security tokens"
---

<h2 class="name">NAME</h2>
<p> westcos-tool &#8211; utility for manipulating data structure on westcos smart card and similar security tokens </p>
<h2>SYNOPSIS</h2>
<p> <code>westcos-tool</code> [OPTIONS]</p>
<h2>DESCRIPTION</h2>
<p> The <code>westcos-tool</code> utility is used to manipulate the westcos data structures on 2 Ko smart cards. Users can create PINs, keys and certificates stored on the token. User PIN authentication is performed for those operations that require it.</p>
<h2>OPTIONS</h2>
<p> <code>-G</code></p>
<dl>
<dt>
<dd> Generate a private key on smart card. The smart card must be not finalized and pin installed (ig. file for pin must be created, see option -i). By default key length is 1536 bits. User authentication is required for this operation.</dl>
<p> <code>-L</code> <i>length</i></p>
<dl>
<dt>
<dd> Change the length of private key, use with <code>-G</code>.</dl>
<p> <code>-i</code></p>
<dl>
<dt>
<dd> Install pin file in token, you must provide pin value with <code>-pin</code>.</dl>
<p> <code>-pin</code> <i>value</i></p>
<dl>
<dt>
<dd> set value of pin.</dl>
<p> <code>-puk</code> <i>value</i></p>
<dl>
<dt>
<dd> set value of puk (or value of new pin for change pin command see <code>-n</code>).</dl>
<p> <code>-n</code></p>
<dl>
<dt>
<dd> Changes a PIN stored on the token. User authentication is required for this operation.</dl>
<p> <code>-u</code></p>
<dl>
<dt>
<dd> Unblocks a PIN stored on the token. Knowledge of the Pin Unblock Key (PUK) is required for this operation.</dl>
<p> <code>-cert</code> <i>file</i></p>
<dl>
<dt>
<dd> Write certificate <i>file</i> in pem format on the card. User authentication is required for this operation.</dl>
<p> <code>-F</code></p>
<dl>
<dt>
<dd> Finalize the card, once finalize default key is invalidate so pin and puk can&#8217;be changed anymore without user authentification. Warning, smart cards not finalized are unsecure because pin can be changed without user authentification (knowledge of default key is enougth).</dl>
<p> <code>-r</code> <i>n</i></p>
<dl>
<dt>
<dd> Forces <code>westcos-tool</code> to use reader number <i>n</i> for operations.</dl>
<p> <code>-gf</code> <i>path</i></p>
<dl>
<dt>
<dd> Get the file <i>path</i> the file is written on disk with <i>path</i> name. User authentication is required for this operation.</dl>
<p> <code>-pf</code> <i>path</i></p>
<dl>
<dt>
<dd> Put the file with name <i>path</i> from disk to card the file is written in <i>path</i>. User authentication is required for this operation.</dl>
<p> <code>-v</code></p>
<dl>
<dt>
<dd> Causes <code>westcos-tool</code> to be more verbose. Specify this flag several times to enable debug output in the OpenSC library.</dl>
<p> <code>-h</code></p>
<dl>
<dt>
<dd> Print help message on screen.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-opensc/">opensc</a>(7)</p>
<h2>AUTHORS</h2>
<p> <code>westcos-tool</code> was written by Francois Leblanc &lt;francois.leblanc [at] cev-sa.com&gt;. </p>
<h2>Index</h2>
