---
title: "groff_mmse(7)"
name: "groff_mmse"
section: "7"
letter: "g"
url: "/docs/linux/man/7-groff_mmse/"
---

<h2>Namn</h2>
<p>groff_mmse &#8211; svenska mm makro för groff</p>
<h2>Syntax</h2>
<p><code>groff</code> <code>-mmse</code> [ <i>flaggor</i>&#8230; ] [ <i>filer</i>&#8230; ]</p>
<h2>Beskrivning</h2>
<p><code>mmse</code> är en svensk variant av <code>mm</code>. Alla texter är översatta. En A4 sida får text som är 13~cm bred, 3.5~cm indragning samt är 28.5~cm hög. Det finns stöd för brevuppställning enligt svensk standard för vänster och högerjusterad text. </p>
<p> <code>COVER</code> kan använda <i>se_ms</i> som argument. Detta ger ett svenskt försättsblad. Se <code><a href="/docs/linux/man/7-groff_mm/">groff_mm</a></code>(7) för övriga detaljer.</p>
<h2>Brev</h2>
<p>Tillgängliga brevtyper:</p>
<dl>
<dt><code>.LT SVV</code></dt>
<dd>Vänsterställd löptext med adressat i position T0 (vänsterställt).</dd>
<dt><code>.LT SVH</code></dt>
<dd>Högerställd löptext med adressat i position T4 (passar fönsterkuvert).</dd></dl>
<p> Följande extra LO-variabler används.</p>
<dl>
<dt><code>.LO DNAMN&nbsp;<wbr></code><i>namn</i></dt>
<dd>Anger dokumentets namn.</dd>
<dt><code>.LO MDAT&nbsp;<wbr></code><i>datum</i></dt>
<dd>Mottagarens datum, anges under <code>Ert datum:</code> (<code>LetMDAT</code>).</dd>
<dt><code>.LO BIL&nbsp;<wbr></code><i>sträng</i></dt>
<dd>Anger bilaga, nummer eller sträng med <code>Bilaga</code> (<code>LetBIL</code>) som prefix.</dd>
<dt><code>.LO KOMP&nbsp;<wbr></code><i>text</i></dt>
<dd>Anger kompletteringsuppgift.</dd>
<dt><code>.LO DBET&nbsp;<wbr></code><i>beteckning</i></dt>
<dd>Anger dokumentbeteckning eller dokumentnummer.</dd>
<dt><code>.LO BET&nbsp;<wbr></code><i>beteckning</i></dt>
<dd>Anger beteckning (ärendebeteckning i form av diarienummer eller liknande).</dd>
<dt><code>.LO SIDOR&nbsp;<wbr></code><i>antal</i></dt>
<dd>Anger totala antalet sidor och skrivs ut efter sidnumret inom parenteser.</dd></dl>
<p> Om makrot <code>.TP</code> är definierat anropas det efter utskrift av brevhuvudet. Där lägger man lämpligen in postadress och annat som brevfot.</p>
<h2>Skrivet Av</h2>
<p>Jörgen Hägg, Lund, Sweden &lt;Jorgen.Hagg [at] axis.se&gt;</p>
<h2>Filer</h2>
<dl>
<dt><code>/usr/share/groff/1.22.2/tmac/mse.tmac</code></dt>
<dd>
</dd><dt><code>/usr/share/groff/1.22.2/tmac/mm/se_*.cov</code></dt>
<dd></dd></dl>
<h2>Se Också</h2>
<p><code><a href="/docs/linux/man/1-groff/">groff</a></code>(1), <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1), <code><a href="/docs/linux/man/1-tbl/">tbl</a></code>(1), <code><a href="/docs/linux/man/1-pic/">pic</a></code>(1), <code><a href="/docs/linux/man/1-eqn/">eqn</a></code>(1)<br/>
 <code><a href="/docs/linux/man/7-groff_mm/">groff_mm</a></code>(7)</p>
