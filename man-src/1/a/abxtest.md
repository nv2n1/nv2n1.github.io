---
title: "abxtest(1)"
name: "abxtest"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abxtest/"
description: "abxtest – double-blind ABX comparison testing script"
---

<h2>NAME</h2>
<p> abxtest &#8211; double-blind ABX comparison testing script</p>
<h2>SYNOPSIS</h2>
<p> <code>abxtest</code> [<code>-n</code> <i>min</i>] [<code>-m</code> <i>max</i>] [<code>-g</code> <i>goal</i>] <i>A-cmd B-cmd</i></p>
<h2>DESCRIPTION</h2>
<p> <code>abxtest</code> is a tool for conducting listening (or other subjective) tests to determine whether a listener can discern a difference between two subjects under test, denoted <code>A</code> and <code>B</code>. </p>
<p> The listener conducts several trials in which an unknown subject, <code>X</code>, is randomly chosen to be either <code>A</code> or <code>B</code>. The probability that <code>X</code> is <code>A</code> or <code>B</code> is the same. The listener must decide whether <code>X</code> sounds the same as <code>A</code> or the same as <code>B</code>. The listener may repeat <code>A</code>, <code>B</code>, and <code>X</code> as many times as necessary before reaching a verdict. </p>
<p> In order to prove the hypothesis that a difference can be discerned between <code>A</code> and <code>B</code>, the listener must disprove the null hypothesis that <code>A</code> sounds the same as <code>B</code>. This is accomplished by correctly identifying <code>X</code> often enough that randomly guessing correctly the same number of times would be statistically improbable. </p>
<p> The <code>A</code> and <code>B</code> subjects for <code>abxtest</code> are actually arbitrary shell commands. The normal mode of use would be to give commands which play two slightly different sounds. The standard output and standard error from each command are suppressed so as not to reveal the identity of <code>X</code>. The listener may interrupt an executing command (usually by pressing <code>^C</code>) without terminating the test.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-n</code> <i>min</i></p>
<dd> Set the minimum number of trials. Trials will continue after this number if the statistical probability goal has not yet been met. The default is 10.</p>
<dt><code>-m</code> <i>max</i></p>
<dd> Set the maximum number of trials. Trials will end after this number even if the statistical probability goal has not been met. The default is 20.</p>
<dt><code>-g</code> <i>goal</i></p>
<dd> Set the minimum statistical probability goal. This is the probability that the number of correct identifications is the same as random guesses. In order to disprove the null hypothesis, the result of the test must be a probability less than or equal to this goal. The default is 0.05.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/dev/random</i></p>
<dd> By default this file is read to generate a random sequence of <code>X</code>.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt>RANDOM_FILE</p>
<dd> If set, the file named by this variable will be read instead of <i>/dev/random</i> to generate a sequence of <code>X</code>.</dl>
<h2>NOTES</h2>
<p> <code>abxtest</code> uses the binomial distribution to accurately calculate the probability that the result is the same as random guesses.</p>
<h2>AUTHOR</h2>
<p> Robert Leslie &lt;rob [at] mars.org&gt; </p>
<h2>Index</h2>
