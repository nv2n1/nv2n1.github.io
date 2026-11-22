---
layout: home
title: "BB Code Editor"
canonical: https://www.systutorials.com/tools/bbeditor/
---

<script src="./jquery.min.js"></script>
<script src="./jquery.wysibb.min.js"></script>
<link rel="stylesheet" href="./theme/st/wbbtheme.css">
<style>
.ad-bb-editor {
  width: 300px;
  height: 250px;
  margin-bottom: 50px;
}
@media (min-width: 801px) {
  .ad-bb-editor {
    float: right;
    margin-left: 50px;
  }
}
@media (max-width: 800px) {
  .ad-bb-editor {
    margin-left: auto;
    margin-right: auto;
  }
}
</style>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5988258742963952"
     crossorigin="anonymous"></script>
<script>
$(document).ready(function() {
  $("#editor").css("height","320px");
  $("#editor").wysibb();
});
</script>

<h1>BB Code Editor</h1>
<p>Welcome to the online bb code editor! Edit your text and click the "[BBCODE]" button to get your bb code.</p>

<textarea id="editor"></textarea>

<h2>BB Code Editor shortcuts</h2>

<div class="ad-bb-editor">
<!-- bb-code-editor-1 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:300px;height:250px"
     data-ad-client="ca-pub-5988258742963952"
     data-ad-slot="4712122667"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div>
<ul>
<li><b>Bold</b>: ctrl + b</li>
<li><b>Italic</b>: ctrl + i</li>
<li><b>Underline</b>: ctrl + u</li>
<li><b>Insert image</b>: ctrl + shift + 1</li>
<li><b>Link</b>: ctrl + shift + 2</li>
<li><b>Code</b>: ctrl + shift + 4</li>
<li><b>Quote</b>: ctrl + shift + 3</li>
</ul>

<h2>BB Code Introduction</h2>
<p><strong>BBCode</strong> (Bulletin Board Code) is a lightweight markup language used to format messages in Internet forums. Introduced in 1998, it uses square bracket tags (e.g., <code>[b]bold[/b]</code>) that are translated into HTML before display.</p>

<h3>Basic Grammar</h3>
<p>BBCode tags follow the pattern <code>[tag]content[/tag]</code> or <code>[tag=value]content[/tag]</code> for tags with parameters. Common tags include:</p>
<ul>
<li><strong>Text formatting</strong>: <code>[b]</code> bold, <code>[i]</code> italic, <code>[u]</code> underline, <code>[s]</code> strikethrough</li>
<li><strong>Links</strong>: <code>[url]https://example.com[/url]</code> or <code>[url=https://example.com]link text[/url]</code></li>
<li><strong>Images</strong>: <code>[img]https://example.com/image.png[/img]</code></li>
<li><strong>Quotes</strong>: <code>[quote]text[/quote]</code> or <code>[quote="author"]text[/quote]</code></li>
<li><strong>Code</strong>: <code>[code]code here[/code]</code> for monospaced formatting</li>
<li><strong>Lists</strong>: <code>[list][*]item 1[*]item 2[/list]</code> (ordered: <code>[list=1]</code>)</li>
<li><strong>Tables</strong>: <code>[table][tr][th]header[/th][/tr][tr][td]cell[/td][/tr][/table]</code></li>
<li><strong>Colors/sizes</strong>: <code>[color=red]text[/color]</code>, <code>[size=14]text[/size]</code></li>
</ul>
<p>Tags can be nested (e.g., <code>[b][i]bold italic[/i][/b]</code>), but must be properly closed in reverse order.</p>

<h2>License</h2>
<p>This tool uses WysiBB v1.5.0, distributed under the MIT license.</p>
<p>BB Code Editor provided by <a href="https://www.systutorials.com/">SysTutorials</a>.</p>
