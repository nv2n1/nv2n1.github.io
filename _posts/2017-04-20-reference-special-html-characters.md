---
title: "HTML Entity Reference Guide"
date: 2017-04-20 08:31:57 +0000
author: "David Yang"
layout: post
categories: [web-development]
canonical: /reference-special-html-characters/
---

HTML entities represent characters that either have special meaning in HTML or benefit from explicit encoding. You have three syntax options:

- **Named entity**: `&name;` (e.g., `&copy;`)
- **Decimal numeric**: `&#number;` (e.g., `&#169;`)
- **Hexadecimal numeric**: `&#xhexcode;` (e.g., `&#xa9;`)

With UTF-8 encoding (the only sensible choice in 2026), most special characters can be typed directly. However, certain characters *must* always be escaped, and named entities significantly improve source code readability.

## Characters That Must Always Be Escaped

These five characters have special meaning in HTML and must be escaped everywhere:

| Character | Named Entity | Numeric | Purpose                          |
|-----------|--------------|---------|----------------------------------|
| `<`       | `&lt;`       | `&#60;` | Prevents tag interpretation      |
| `>`       | `&gt;`       | `&#62;` | Prevents tag interpretation      |
| `&`       | `&amp;`      | `&#38;` | Required before entity-like text |
| `"`       | `&quot;`     | `&#34;` | In double-quoted attributes      |
| `'`       | `&apos;`     | `&#39;` | In single-quoted attributes      |

### Escaping Examples

``` html
<!-- Text content with comparison operators -->
<p>Use &lt; and &gt; for comparisons: x &lt; 10 and y &gt; 5</p>

<!-- Ampersand before entity-like text -->
<p>Johnson &amp; Sons &mdash; Est. 1985</p>

<!-- Ampersand in URLs (attribute values) -->
<a href="search.php?q=fish&amp;chips">Search results</a>

<!-- Quotes in attributes -->
<p title="Use &quot;quotes&quot; carefully">Hover here</p>

<!-- JSON in data attributes -->
<div data-config='{"message": "&lt;error&gt;"}'></div>
```

The ampersand rule is critical: whenever `&` is followed by letters or numbers that resemble an entity pattern, escape it. Modern browsers are somewhat forgiving, but explicit escaping prevents rendering surprises.

## When to Use Named vs. UTF-8 Characters

**Use named entities for readability** when maintaining human-readable source code matters:

``` html
<footer>
  &copy; 2026 &mdash; All rights reserved &mdash; €50/month
</footer>

<p>Price: &pound;99 &times; 12 = &pound;1,188</p>
```

**Use direct UTF-8 characters** when you’re confident about file encoding (always declare it):

``` html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Example</title>
</head>
<body>
  <footer>
    © 2026 — All rights reserved — €50/month
  </footer>

  <p>Price: £99 × 12 = £1,188</p>
</body>
</html>
```

Named entities are self-documenting and work reliably across all browsers. Direct UTF-8 characters are cleaner in rendered output and easier to edit. Choose based on your workflow.

## Punctuation and Typographic Entities

| Description        | Named Entity | Character |
|--------------------|--------------|-----------|
| Left single quote  | `&lsquo;`    | ‘         |
| Right single quote | `&rsquo;`    | ‘         |
| Left double quote  | `&ldquo;`    | “         |
| Right double quote | `&rdquo;`    | “         |
| En dash            | `&ndash;`    | –         |
| Em dash            | `&mdash;`    | —         |
| Ellipsis           | `&hellip;`   | …         |
| Non-breaking space | `&nbsp;`     | (space)   |

Use smart quotes and proper dashes in body text for professional typography:

``` html
<p>&ldquo;The quick brown fox,&rdquo; she said &mdash; perfectly phrased.</p>

<p>Price range: $50&ndash;$100 (use en dash for ranges)</p>

<p>Wait for it&hellip;</p>
```

## Currency Symbols

| Description    | Named Entity | Character |
|----------------|--------------|-----------|
| Euro           | `&euro;`     | €         |
| Pound sterling | `&pound;`    | £         |
| Yen            | `&yen;`      | ¥         |
| Cent           | `&cent;`     | ¢         |

## Mathematical Symbols

| Description            | Named Entity | Character |
|------------------------|--------------|-----------|
| Plus or minus          | `&plusmn;`   | ±         |
| Multiplication         | `&times;`    | ×         |
| Division               | `&divide;`   | ÷         |
| Fraction one-half      | `&frac12;`   | ½         |
| Fraction one-fourth    | `&frac14;`   | ¼         |
| Fraction three-fourths | `&frac34;`   | ¾         |
| Superscript 1          | `&sup1;`     | ¹         |
| Superscript 2          | `&sup2;`     | ²         |
| Superscript 3          | `&sup3;`     | ³         |
| Degree                 | `&deg;`      | °         |
| Micro                  | `&micro;`    | µ         |
| Per mille              | `&permil;`   | ‰         |
| Infinity               | `&infin;`    | ∞         |
| Square root            | `&radic;`    | √         |
| Not equal              | `&ne;`       | ≠         |
| Less than or equal     | `&le;`       | ≤         |
| Greater than or equal  | `&ge;`       | ≥         |

## Arrows

| Direction  | Named Entity | Character |
|------------|--------------|-----------|
| Leftward   | `&larr;`     | ←         |
| Rightward  | `&rarr;`     | →         |
| Upward     | `&uarr;`     | ↑         |
| Downward   | `&darr;`     | ↓         |
| Left-right | `&harr;`     | ↔         |

## Greek Letters

| Letter  | Named Entity | Character |
|---------|--------------|-----------|
| Alpha   | `&alpha;`    | α         |
| Beta    | `&beta;`     | β         |
| Gamma   | `&gamma;`    | γ         |
| Delta   | `&delta;`    | δ         |
| Epsilon | `&epsilon;`  | ε         |
| Pi      | `&pi;`       | π         |
| Sigma   | `&sigma;`    | σ         |
| Omega   | `&omega;`    | ω         |

## Accented Characters

### Uppercase

| Description  | Named Entity | Character |
|--------------|--------------|-----------|
| A grave      | `&Agrave;`   | À         |
| A acute      | `&Aacute;`   | Á         |
| A circumflex | `&Acirc;`    | Â         |
| A tilde      | `&Atilde;`   | Ã         |
| A umlaut     | `&Auml;`     | Ä         |
| C cedilla    | `&Ccedil;`   | Ç         |
| E grave      | `&Egrave;`   | È         |
| E acute      | `&Eacute;`   | É         |
| N tilde      | `&Ntilde;`   | Ñ         |
| O umlaut     | `&Ouml;`     | Ö         |
| U umlaut     | `&Uuml;`     | Ü         |

### Lowercase

| Description      | Named Entity | Character |
|------------------|--------------|-----------|
| a grave          | `&agrave;`   | à         |
| a acute          | `&aacute;`   | á         |
| a circumflex     | `&acirc;`    | â         |
| a tilde          | `&atilde;`   | ã         |
| a umlaut         | `&auml;`     | ä         |
| c cedilla        | `&ccedil;`   | ç         |
| e grave          | `&egrave;`   | è         |
| e acute          | `&eacute;`   | é         |
| n tilde          | `&ntilde;`   | ñ         |
| o umlaut         | `&ouml;`     | ö         |
| u umlaut         | `&uuml;`     | ü         |
| Sharp s (German) | `&szlig;`    | ß         |

## Other Common Entities

| Description          | Named Entity | Character |
|----------------------|--------------|-----------|
| Copyright            | `&copy;`     | ©         |
| Registered trademark | `&reg;`      | ®         |
| Trademark            | `&trade;`    | ™         |
| Section              | `&sect;`     | §         |
| Paragraph            | `&para;`     | ¶         |
| Dagger               | `&dagger;`   | †         |
| Double dagger        | `&Dagger;`   | ‡         |
| Bullet               | `&bull;`     | •         |
| Middle dot           | `&middot;`   | ·         |
| Spade                | `&spades;`   | ♠         |
| Club                 | `&clubs;`    | ♣         |
| Heart                | `&hearts;`   | ♥         |
| Diamond              | `&diams;`    | ♦         |
| Inverted !           | `&iexcl;`    | ¡         |
| Inverted ?           | `&iquest;`   | ¿         |

## Best Practices

**Always declare UTF-8 encoding.** This is non-negotiable:

``` html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Example</title>
</head>
<body>
  <p>© 2026 Company — All rights reserved</p>
</body>
</html>
```

**Escape the five critical characters everywhere.** This applies in text content, attributes, data attributes, and any context where HTML is parsed:

``` html
<!-- Text content -->
<p>Use &lt; and &gt; for comparisons</p>

<!-- Attributes -->
<a href="search.php?q=fish&amp;chips">Search</a>
<input type="text" placeholder="Enter &quot;name&quot;">

<!-- Data attributes and embedded markup -->
<div data-config='{"error": "&lt;critical&gt;"}'></div>
```

**Use named entities for improved source readability** when you need to maintain the code long-term:

``` html
<footer>&copy; 2026 &mdash; All rights reserved</footer>
```

**Be cautious with ampersands.** Any ampersand followed by letters or numbers that look entity-like should be escaped:

``` html
<!-- Bad: Could be misinterpreted -->
<p>Fish & chips</p>

<!-- Good: Explicitly escaped -->
<p>Fish &amp; chips</p>

<!-- Safe: No entity-like pattern follows -->
<p>Q&A section</p>
```

Most modern browsers tolerate unescaped ampersands in safe contexts, but explicit escaping is the professional approach and prevents edge cases.

**Replace deprecated entities with CSS.** The `&shy;` (soft hyphen) entity is rarely needed. Use modern CSS properties instead:

``` css
.content {
  word-break: break-word;
  hyphens: auto;
  overflow-wrap: break-word;
}
```

This approach provides better control over text wrapping on responsive layouts and works reliably across all devices.
