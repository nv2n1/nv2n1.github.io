---
title: "clang-format-diff-10(1)"
name: "clang-format-diff-10"
section: "1"
letter: "c"
url: "/docs/linux/man/1-clang-format-diff-10/"
description: "clang-format-diff.py – manual page for clang-format-diff.py 10"
---

<h2 class="name">NAME</h2>
<p> clang-format-diff.py &#8211; manual page for clang-format-diff.py 10 </p>
<h2>DESCRIPTION</h2>
<p> usage: clang-format-diff.py [-h] [-i] [-p NUM] [-regex PATTERN]</p>
<dl>
<dt>[-iregex PATTERN] [-sort-includes] [-v]</dt>
<dd> [-style STYLE] [-binary BINARY]</dd></dl>
<p> This script reads input from a unified diff and reformats all the changed lines. This is useful to reformat all the lines touched by a specific patch. Example usage for git/svn users:</p>
<dl>
<dt>
</dt><dd> git diff <code>-U0</code> <code>&#8211;no-color</code> HEAD^ | clang-format-diff.py <code>-p1</code> <code>-i</code> svn diff <code>&#8211;diff-cmd</code>=<i>,diff/</i> <code>-x-U0</code> | clang-format-diff.py <code>-i</code></dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help message and exit</dd>
<dt><code>-i</code></dt>
<dd> apply edits to files instead of displaying a diff</dd>
<dt><code>-p</code> NUM</dt>
<dd> strip the smallest prefix containing P slashes</dd>
<dt><code>-regex</code> PATTERN</dt>
<dd> custom pattern selecting file paths to reformat (case sensitive, overrides <code>-iregex</code>)</dd>
<dt><code>-iregex</code> PATTERN</dt>
<dd> custom pattern selecting file paths to reformat (case insensitive, overridden by <code>-regex</code>)</dd>
<dt><code>-sort-includes</code></dt>
<dd> let clang-format sort include blocks</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> be more verbose, ineffective without <code>-i</code></dd>
<dt><code>-style</code> STYLE</dt>
<dd> formatting style to apply (LLVM, Google, Chromium, Mozilla, WebKit)</dd>
<dt><code>-binary</code> BINARY</dt>
<dd> location of binary to use for clang-format </dd>
</dl>
