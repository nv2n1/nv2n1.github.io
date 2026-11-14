---
title: "filecheck-14(1)"
name: "filecheck-14"
section: "1"
letter: "f"
url: "/docs/linux/man/1-filecheck-14/"
description: "FileCheck – Flexible pattern matching file verifier"
---

<p>FileCheck &#8211; Flexible pattern matching file verifier </p>
<h2>Synopsis</h2>
<p><code>FileCheck</code> <i>match-filename</i> [<i>–check-prefix=XXX</i>] [<i>–strict-whitespace</i>]</p>
<h2>Description</h2>
<p><code>FileCheck</code> reads two files (one from standard input, and one specified on the command line) and uses one to verify the other. This behavior is particularly useful for the testsuite, which wants to verify that the output of some tool (e.g. <code>llc</code>) contains the expected information (for example, a movsd from esp or whatever is interesting). This is similar to using <code>grep</code>, but it is optimized for matching multiple different inputs in one file in a specific order. </p>
<p> The <code>match-filename</code> file specifies the file that contains the patterns to match. The file to verify is read from standard input unless the <i>&#8211;input-file</i> option is used.</p>
<h2>Options</h2>
<p>Options are parsed from the environment variable <code>FILECHECK_OPTS</code> and from the command line.</p>
<dl>
<dt><code>-help</code></p>
<dd>Print a summary of command line options.</p>
<dt><code>&#8211;check-prefix prefix</code></p>
<dd>FileCheck searches the contents of <code>match-filename</code> for patterns to match. By default, these patterns are prefixed with “<code>CHECK:</code>”. If you’d like to use a different prefix (e.g. because the same input file is checking multiple different tool or options), the <i>&#8211;check-prefix</i> argument allows you to specify (without the trailing “<code>:</code>”) one or more prefixes to match. Multiple prefixes are useful for tests which might change for different run options, but most lines remain the same. </p>
<p> FileCheck does not permit duplicate prefixes, even if one is a check prefix and one is a comment prefix (see <i>&#8211;comment-prefixes</i> below).</p>
<dt><code>&#8211;check-prefixes prefix1,prefix2,&#8230;</code></p>
<dd>An alias of <i>&#8211;check-prefix</i> that allows multiple prefixes to be specified as a comma separated list.</p>
<dt><code>&#8211;comment-prefixes prefix1,prefix2,&#8230;</code></p>
<dd>By default, FileCheck ignores any occurrence in <code>match-filename</code> of any check prefix if it is preceded on the same line by “<code>COM:</code>” or “<code>RUN:</code>”. See the section <i>The “COM:” directive</i> for usage details. </p>
<p> These default comment prefixes can be overridden by <i>&#8211;comment-prefixes</i> if they are not appropriate for your testing environment. However, doing so is not recommended in LLVM’s LIT-based test suites, which should be easier to maintain if they all follow a consistent comment style. In that case, consider proposing a change to the default comment prefixes instead.</p>
<dt><code>&#8211;allow-unused-prefixes</code></p>
<dd>This option controls the behavior when using more than one prefix as specified by <i>&#8211;check-prefix</i> or <i>&#8211;check-prefixes</i>, and some of these prefixes are missing in the test file. If true, this is allowed, if false, FileCheck will report an error, listing the missing prefixes. </p>
<p> It is currently, temporarily, true by default, and will be subsequently switched to false.</p>
<dt><code>&#8211;input-file filename</code></p>
<dd>File to check (defaults to stdin).</p>
<dt><code>&#8211;match-full-lines</code></p>
<dd>By default, FileCheck allows matches of anywhere on a line. This option will require all positive matches to cover an entire line. Leading and trailing whitespace is ignored, unless <i>&#8211;strict-whitespace</i> is also specified. (Note: negative matches from <code>CHECK-NOT</code> are not affected by this option!) </p>
<p> Passing this option is equivalent to inserting <code>&#123;&#123;^ *}}</code> or <code>&#123;&#123;^}}</code> before, and <code>&#123;&#123; *$}}</code> or <code>&#123;&#123;$}}</code> after every positive check pattern.</p>
<dt><code>&#8211;strict-whitespace</code></p>
<dd>By default, FileCheck canonicalizes input horizontal whitespace (spaces and tabs) which causes it to ignore these differences (a space will match a tab). The <i>&#8211;strict-whitespace</i> argument disables this behavior. End-of-line sequences are canonicalized to UNIX-style <code>
</code> in all modes.</p>
<dt><code>&#8211;ignore-case</code></p>
<dd>By default, FileCheck uses case-sensitive matching. This option causes FileCheck to use case-insensitive matching.</p>
<dt><code>&#8211;implicit-check-not check-pattern</code></p>
<dd>Adds implicit negative checks for the specified patterns between positive checks. The option allows writing stricter tests without stuffing them with <code>CHECK-NOT</code>s. </p>
<p> For example, “<code>&#8211;implicit-check-not warning:</code>” can be useful when testing diagnostic messages from tools that don’t have an option similar to <code>clang -verify</code>. With this option FileCheck will verify that input does not contain warnings not covered by any <code>CHECK:</code> patterns.</p>
<dt><code>&#8211;dump-input &lt;value&gt;</code></p>
<dd>Dump input to stderr, adding annotations representing currently enabled diagnostics. When there are multiple occurrences of this option, the <code>&lt;value&gt;</code> that appears earliest in the list below has precedence. The default is <code>fail</code>.</p>
<dt>&bull;</p>
<dd><code>help</code> &#8211; Explain input dump and quit</p>
<dt>&bull;</p>
<dd><code>always</code> &#8211; Always dump input</p>
<dt>&bull;</p>
<dd><code>fail</code> &#8211; Dump input on failure</p>
<dt>&bull;</p>
<dd><code>never</code> &#8211; Never dump input</p>
<dt><code>&#8211;dump-input-context &lt;N&gt;</code></p>
<dd>In the dump requested by <code>&#8211;dump-input</code>, print <code>&lt;N&gt;</code> input lines before and <code>&lt;N&gt;</code> input lines after any lines specified by <code>&#8211;dump-input-filter</code>. When there are multiple occurrences of this option, the largest specified <code>&lt;N&gt;</code> has precedence. The default is 5.</p>
<dt><code>&#8211;dump-input-filter &lt;value&gt;</code></p>
<dd>In the dump requested by <code>&#8211;dump-input</code>, print only input lines of kind <code>&lt;value&gt;</code> plus any context specified by <code>&#8211;dump-input-context</code>. When there are multiple occurrences of this option, the <code>&lt;value&gt;</code> that appears earliest in the list below has precedence. The default is <code>error</code> when <code>&#8211;dump-input=fail</code>, and it’s <code>all</code> when <code>&#8211;dump-input=always</code>.</p>
<dt>&bull;</p>
<dd><code>all</code> &#8211; All input lines</p>
<dt>&bull;</p>
<dd><code>annotation-full</code> &#8211; Input lines with annotations</p>
<dt>&bull;</p>
<dd><code>annotation</code> &#8211; Input lines with starting points of annotations</p>
<dt>&bull;</p>
<dd><code>error</code> &#8211; Input lines with starting points of error annotations</p>
<dt><code>&#8211;enable-var-scope</code></p>
<dd>Enables scope for regex variables. </p>
<p> Variables with names that start with <code>$</code> are considered global and remain set throughout the file. </p>
<p> All other variables get undefined after each encountered <code>CHECK-LABEL</code>.</p>
<dt><code>-D&lt;VAR=VALUE&gt;</code></p>
<dd>Sets a filecheck pattern variable <code>VAR</code> with value <code>VALUE</code> that can be used in <code>CHECK:</code> lines.</p>
<dt><code>-D#&lt;FMT&gt;,&lt;NUMVAR&gt;=&lt;NUMERIC EXPRESSION&gt;</code></p>
<dd>Sets a filecheck numeric variable <code>NUMVAR</code> of matching format <code>FMT</code> to the result of evaluating <code>&lt;NUMERIC EXPRESSION&gt;</code> that can be used in <code>CHECK:</code> lines. See section <code>FileCheck Numeric Variables and Expressions</code> for details on supported numeric expressions.</p>
<dt><code>-version</code></p>
<dd>Show the version number of this program.</p>
<dt><code>-v</code></p>
<dd>Print good directive pattern matches. However, if <code>-dump-input=fail</code> or <code>-dump-input=always</code>, add those matches as input annotations instead.</p>
<dt><code>-vv</code></p>
<dd>Print information helpful in diagnosing internal FileCheck issues, such as discarded overlapping <code>CHECK-DAG:</code> matches, implicit EOF pattern matches, and <code>CHECK-NOT:</code> patterns that do not have matches. Implies <code>-v</code>. However, if <code>-dump-input=fail</code> or <code>-dump-input=always</code>, just add that information as input annotations instead.</p>
<dt><code>&#8211;allow-deprecated-dag-overlap</code></p>
<dd>Enable overlapping among matches in a group of consecutive <code>CHECK-DAG:</code> directives. This option is deprecated and is only provided for convenience as old tests are migrated to the new non-overlapping <code>CHECK-DAG:</code> implementation.</p>
<dt><code>&#8211;allow-empty</code></p>
<dd>Allow checking empty input. By default, empty input is rejected.</p>
<dt><code>&#8211;color</code></p>
<dd>Use colors in output (autodetected by default).</dl>
<h2>Exit Status</h2>
<p>If <code>FileCheck</code> verifies that the file matches the expected contents, it exits with 0. Otherwise, if not, or if an error occurs, it will exit with a non-zero value.</p>
<h2>Tutorial</h2>
<p>FileCheck is typically used from LLVM regression tests, being invoked on the RUN line of the test. A simple example of using FileCheck from a RUN line looks like this: </p>
<pre>; RUN: llvm-as &lt; %s | llc -march=x86-64 | FileCheck %s</pre>
<p>This syntax says to pipe the current file (”<code>%s</code>”) into <code>llvm-as</code>, pipe that into <code>llc</code>, then pipe the output of <code>llc</code> into <code>FileCheck</code>. This means that FileCheck will be verifying its standard input (the llc output) against the filename argument specified (the original <code>.ll</code> file specified by “<code>%s</code>”). To see how this works, let’s look at the rest of the <code>.ll</code> file (after the RUN line): </p>
<pre>define void @sub1(i32* %p, i32 %v) {
entry:
; CHECK: sub1:
; CHECK: subl
 %0 = tail call i32 @llvm.atomic.load.sub.i32.p0i32(i32* %p, i32 %v)
 ret void
}
define void @inc4(i64* %p) {
entry:
; CHECK: inc4:
; CHECK: incq
 %0 = tail call i64 @llvm.atomic.load.add.i64.p0i64(i64* %p, i64 1)
 ret void
}</pre>
<p>Here you can see some “<code>CHECK:</code>” lines specified in comments. Now you can see how the file is piped into <code>llvm-as</code>, then <code>llc</code>, and the machine code output is what we are verifying. FileCheck checks the machine code output to verify that it matches what the “<code>CHECK:</code>” lines specify. </p>
<p> The syntax of the “<code>CHECK:</code>” lines is very simple: they are fixed strings that must occur in order. FileCheck defaults to ignoring horizontal whitespace differences (e.g. a space is allowed to match a tab) but otherwise, the contents of the “<code>CHECK:</code>” line is required to match some thing in the test file exactly. </p>
<p> One nice thing about FileCheck (compared to grep) is that it allows merging test cases together into logical groups. For example, because the test above is checking for the “<code>sub1:</code>” and “<code>inc4:</code>” labels, it will not match unless there is a “<code>subl</code>” in between those labels. If it existed somewhere else in the file, that would not count: “<code>grep subl</code>” matches if “<code>subl</code>” exists anywhere in the file.</p>
<h3>The FileCheck -check-prefix option</h3>
<p>The FileCheck <i>-check-prefix</i> option allows multiple test configurations to be driven from one <i>.ll</i> file. This is useful in many circumstances, for example, testing different architectural variants with <code>llc</code>. Here’s a simple example: </p>
<pre>; RUN: llvm-as &lt; %s | llc -mtriple=i686-apple-darwin9 -mattr=sse41 \
; RUN: | FileCheck %s -check-prefix=X32
; RUN: llvm-as &lt; %s | llc -mtriple=x86_64-apple-darwin9 -mattr=sse41 \
; RUN: | FileCheck %s -check-prefix=X64
define &lt;4 x i32&gt; @pinsrd_1(i32 %s, &lt;4 x i32&gt; %tmp) nounwind {
 %tmp1 = insertelement &lt;4 x i32&gt;; %tmp, i32 %s, i32 1
 ret &lt;4 x i32&gt; %tmp1
; X32: pinsrd_1:
; X32: pinsrd $1, 4(%esp), %xmm0
; X64: pinsrd_1:
; X64: pinsrd $1, %edi, %xmm0
}</pre>
<p>In this case, we’re testing that we get the expected code generation with both 32-bit and 64-bit code generation.</p>
<h3>The “COM:” directive</h3>
<p>Sometimes you want to disable a FileCheck directive without removing it entirely, or you want to write comments that mention a directive by name. The “<code>COM:</code>” directive makes it easy to do this. For example, you might have: </p>
<pre>; X32: pinsrd_1:
; X32: pinsrd $1, 4(%esp), %xmm0
; COM: FIXME: X64 isn't working correctly yet for this part of codegen, but
; COM: X64 will have something similar to X32:
; COM:
; COM: X64: pinsrd_1:
; COM: X64: pinsrd $1, %edi, %xmm0</pre>
<p>Without “<code>COM:</code>”, you would need to use some combination of rewording and directive syntax mangling to prevent FileCheck from recognizing the commented occurrences of “<code>X32:</code>” and “<code>X64:</code>” above as directives. Moreover, FileCheck diagnostics have been proposed that might complain about the above occurrences of “<code>X64</code>” that don’t have the trailing “<code>:</code>” because they look like directive typos. Dodging all these problems can be tedious for a test author, and directive syntax mangling can make the purpose of test code unclear. “<code>COM:</code>” avoids all these problems. </p>
<p> A few important usage notes:</p>
<dl>
<dt>&bull;</p>
<dd>“<code>COM:</code>” within another directive’s pattern does <i>not</i> comment out the remainder of the pattern. For example: </p>
<pre>; X32: pinsrd $1, 4(%esp), %xmm0 COM: This is part of the X32 pattern!</pre>
<p>If you need to temporarily comment out part of a directive’s pattern, move it to another line. The reason is that FileCheck parses “<code>COM:</code>” in the same manner as any other directive: only the first directive on the line is recognized as a directive.</p>
<dt>&bull;</p>
<dd>For the sake of LIT, FileCheck treats “<code>RUN:</code>” just like “<code>COM:</code>”. If this is not suitable for your test environment, see <i>&#8211;comment-prefixes</i>.</p>
<dt>&bull;</p>
<dd>FileCheck does not recognize “<code>COM</code>”, “<code>RUN</code>”, or any user-defined comment prefix as a comment directive if it’s combined with one of the usual check directive suffixes, such as “<code>-NEXT:</code>” or “<code>-NOT:</code>”, discussed below. FileCheck treats such a combination as plain text instead. If it needs to act as a comment directive for your test environment, define it as such with <i>&#8211;comment-prefixes</i>.</dl>
<h3>The “CHECK-NEXT:” directive</h3>
<p>Sometimes you want to match lines and would like to verify that matches happen on exactly consecutive lines with no other lines in between them. In this case, you can use “<code>CHECK:</code>” and “<code>CHECK-NEXT:</code>” directives to specify this. If you specified a custom check prefix, just use “<code>&lt;PREFIX&gt;-NEXT:</code>”. For example, something like this works as you’d expect: </p>
<pre>define void @t2(&lt;2 x double&gt;* %r, &lt;2 x double&gt;* %A, double %B) {
 %tmp3 = load &lt;2 x double&gt;* %A, align 16
 %tmp7 = insertelement &lt;2 x double&gt; undef, double %B, i32 0
 %tmp9 = shufflevector &lt;2 x double&gt; %tmp3,
 &lt;2 x double&gt; %tmp7,
 &lt;2 x i32&gt; &lt; i32 0, i32 2 &gt;
 store &lt;2 x double&gt; %tmp9, &lt;2 x double&gt;* %r, align 16
 ret void
; CHECK: t2:
; CHECK: movl 8(%esp), %eax
; CHECK-NEXT: movapd (%eax), %xmm0
; CHECK-NEXT: movhpd 12(%esp), %xmm0
; CHECK-NEXT: movl 4(%esp), %eax
; CHECK-NEXT: movapd %xmm0, (%eax)
; CHECK-NEXT: ret
}</pre>
<p>“<code>CHECK-NEXT:</code>” directives reject the input unless there is exactly one newline between it and the previous directive. A “<code>CHECK-NEXT:</code>” cannot be the first directive in a file.</p>
<h3>The “CHECK-SAME:” directive</h3>
<p>Sometimes you want to match lines and would like to verify that matches happen on the same line as the previous match. In this case, you can use “<code>CHECK:</code>” and “<code>CHECK-SAME:</code>” directives to specify this. If you specified a custom check prefix, just use “<code>&lt;PREFIX&gt;-SAME:</code>”. </p>
<p> “<code>CHECK-SAME:</code>” is particularly powerful in conjunction with “<code>CHECK-NOT:</code>” (described below). </p>
<p> For example, the following works like you’d expect: </p>
<pre>!0 = !DILocation(line: 5, scope: !1, inlinedAt: !2)
; CHECK: !DILocation(line: 5,
; CHECK-NOT: column:
; CHECK-SAME: scope: ![[SCOPE:[0-9]+]]</pre>
<p>“<code>CHECK-SAME:</code>” directives reject the input if there are any newlines between it and the previous directive. </p>
<p> “<code>CHECK-SAME:</code>” is also useful to avoid writing matchers for irrelevant fields. For example, suppose you’re writing a test which parses a tool that generates output like this: </p>
<pre>Name: foo
Field1: ...
Field2: ...
Field3: ...
Value: 1
Name: bar
Field1: ...
Field2: ...
Field3: ...
Value: 2
Name: baz
Field1: ...
Field2: ...
Field3: ...
Value: 1</pre>
<p>To write a test that verifies <code>foo</code> has the value <code>1</code>, you might first write this: </p>
<pre>CHECK: Name: foo
CHECK: Value: 1&#123;&#123;$}}</pre>
<p>However, this would be a bad test: if the value for <code>foo</code> changes, the test would still pass because the “<code>CHECK: Value: 1</code>” line would match the value from <code>baz</code>. To fix this, you could add <code>CHECK-NEXT</code> matchers for every <code>FieldN:</code> line, but that would be verbose, and need to be updated when <code>Field4</code> is added. A more succinct way to write the test using the “<code>CHECK-SAME:</code>” matcher would be as follows: </p>
<pre>CHECK: Name: foo
CHECK: Value:
CHECK-SAME: &#123;&#123; 1$}}</pre>
<p>This verifies that the <i>next</i> time “<code>Value:</code>” appears in the output, it has the value <code>1</code>. </p>
<p> Note: a “<code>CHECK-SAME:</code>” cannot be the first directive in a file.</p>
<h3>The “CHECK-EMPTY:” directive</h3>
<p>If you need to check that the next line has nothing on it, not even whitespace, you can use the “<code>CHECK-EMPTY:</code>” directive. </p>
<pre>declare void @foo()
declare void @bar()
; CHECK: foo
; CHECK-EMPTY:
; CHECK-NEXT: bar</pre>
<p>Just like “<code>CHECK-NEXT:</code>” the directive will fail if there is more than one newline before it finds the next blank line, and it cannot be the first directive in a file.</p>
<h3>The “CHECK-NOT:” directive</h3>
<p>The “<code>CHECK-NOT:</code>” directive is used to verify that a string doesn’t occur between two matches (or before the first match, or after the last match). For example, to verify that a load is removed by a transformation, a test like this can be used: </p>
<pre>define i8 @coerce_offset0(i32 %V, i32* %P) {
 store i32 %V, i32* %P
 %P2 = bitcast i32* %P to i8*
 %P3 = getelementptr i8* %P2, i32 2
 %A = load i8* %P3
 ret i8 %A
; CHECK: @coerce_offset0
; CHECK-NOT: load
; CHECK: ret i8
}</pre>
<h3>The “CHECK-COUNT:” directive</h3>
<p>If you need to match multiple lines with the same pattern over and over again you can repeat a plain <code>CHECK:</code> as many times as needed. If that looks too boring you can instead use a counted check “<code>CHECK-COUNT-&lt;num&gt;:</code>”, where <code>&lt;num&gt;</code> is a positive decimal number. It will match the pattern exactly <code>&lt;num&gt;</code> times, no more and no less. If you specified a custom check prefix, just use “<code>&lt;PREFIX&gt;-COUNT-&lt;num&gt;:</code>” for the same effect. Here is a simple example: </p>
<pre>Loop at depth 1
Loop at depth 1
Loop at depth 1
Loop at depth 1
 Loop at depth 2
 Loop at depth 3
; CHECK-COUNT-6: Loop at depth &#123;&#123;[0-9]+}}
; CHECK-NOT: Loop at depth &#123;&#123;[0-9]+}}</pre>
<h3>The “CHECK-DAG:” directive</h3>
<p>If it’s necessary to match strings that don’t occur in a strictly sequential order, “<code>CHECK-DAG:</code>” could be used to verify them between two matches (or before the first match, or after the last match). For example, clang emits vtable globals in reverse order. Using <code>CHECK-DAG:</code>, we can keep the checks in the natural order: </p>
<pre>// RUN: %clang_cc1 %s -emit-llvm -o - | FileCheck %s
struct Foo { virtual void method(); };
Foo f; // emit vtable
// CHECK-DAG: @_ZTV3Foo =
struct Bar { virtual void method(); };
Bar b;
// CHECK-DAG: @_ZTV3Bar =</pre>
<p><code>CHECK-NOT:</code> directives could be mixed with <code>CHECK-DAG:</code> directives to exclude strings between the surrounding <code>CHECK-DAG:</code> directives. As a result, the surrounding <code>CHECK-DAG:</code> directives cannot be reordered, i.e. all occurrences matching <code>CHECK-DAG:</code> before <code>CHECK-NOT:</code> must not fall behind occurrences matching <code>CHECK-DAG:</code> after <code>CHECK-NOT:</code>. For example, </p>
<pre>; CHECK-DAG: BEFORE
; CHECK-NOT: NOT
; CHECK-DAG: AFTER</pre>
<p>This case will reject input strings where <code>BEFORE</code> occurs after <code>AFTER</code>. </p>
<p> With captured variables, <code>CHECK-DAG:</code> is able to match valid topological orderings of a DAG with edges from the definition of a variable to its use. It’s useful, e.g., when your test cases need to match different output sequences from the instruction scheduler. For example, </p>
<pre>; CHECK-DAG: add [[REG1:r[0-9]+]], r1, r2
; CHECK-DAG: add [[REG2:r[0-9]+]], r3, r4
; CHECK: mul r5, [[REG1]], [[REG2]]</pre>
<p>In this case, any order of that two <code>add</code> instructions will be allowed. </p>
<p> If you are defining <i>and</i> using variables in the same <code>CHECK-DAG:</code> block, be aware that the definition rule can match <i>after</i> its use. </p>
<p> So, for instance, the code below will pass: </p>
<pre>; CHECK-DAG: vmov.32 [[REG2:d[0-9]+]][0]
; CHECK-DAG: vmov.32 [[REG2]][1]
vmov.32 d0[1]
vmov.32 d0[0]</pre>
<p>While this other code, will not: </p>
<pre>; CHECK-DAG: vmov.32 [[REG2:d[0-9]+]][0]
; CHECK-DAG: vmov.32 [[REG2]][1]
vmov.32 d1[1]
vmov.32 d0[0]</pre>
<p>While this can be very useful, it’s also dangerous, because in the case of register sequence, you must have a strong order (read before write, copy before use, etc). If the definition your test is looking for doesn’t match (because of a bug in the compiler), it may match further away from the use, and mask real bugs away. </p>
<p> In those cases, to enforce the order, use a non-DAG directive between DAG-blocks. </p>
<p> A <code>CHECK-DAG:</code> directive skips matches that overlap the matches of any preceding <code>CHECK-DAG:</code> directives in the same <code>CHECK-DAG:</code> block. Not only is this non-overlapping behavior consistent with other directives, but it’s also necessary to handle sets of non-unique strings or patterns. For example, the following directives look for unordered log entries for two tasks in a parallel program, such as the OpenMP runtime: </p>
<pre>// CHECK-DAG: [[THREAD_ID:[0-9]+]]: task_begin
// CHECK-DAG: [[THREAD_ID]]: task_end
//
// CHECK-DAG: [[THREAD_ID:[0-9]+]]: task_begin
// CHECK-DAG: [[THREAD_ID]]: task_end</pre>
<p>The second pair of directives is guaranteed not to match the same log entries as the first pair even though the patterns are identical and even if the text of the log entries is identical because the thread ID manages to be reused.</p>
<h3>The “CHECK-LABEL:” directive</h3>
<p>Sometimes in a file containing multiple tests divided into logical blocks, one or more <code>CHECK:</code> directives may inadvertently succeed by matching lines in a later block. While an error will usually eventually be generated, the check flagged as causing the error may not actually bear any relationship to the actual source of the problem. </p>
<p> In order to produce better error messages in these cases, the “<code>CHECK-LABEL:</code>” directive can be used. It is treated identically to a normal <code>CHECK</code> directive except that FileCheck makes an additional assumption that a line matched by the directive cannot also be matched by any other check present in <code>match-filename</code>; this is intended to be used for lines containing labels or other unique identifiers. Conceptually, the presence of <code>CHECK-LABEL</code> divides the input stream into separate blocks, each of which is processed independently, preventing a <code>CHECK:</code> directive in one block matching a line in another block. If <code>&#8211;enable-var-scope</code> is in effect, all local variables are cleared at the beginning of the block. </p>
<p> For example, </p>
<pre>define %struct.C* @C_ctor_base(%struct.C* %this, i32 %x) {
entry:
; CHECK-LABEL: C_ctor_base:
; CHECK: mov [[SAVETHIS:r[0-9]+]], r0
; CHECK: bl A_ctor_base
; CHECK: mov r0, [[SAVETHIS]]
 %0 = bitcast %struct.C* %this to %struct.A*
 %call = tail call %struct.A* @A_ctor_base(%struct.A* %0)
 %1 = bitcast %struct.C* %this to %struct.B*
 %call2 = tail call %struct.B* @B_ctor_base(%struct.B* %1, i32 %x)
 ret %struct.C* %this
}
define %struct.D* @D_ctor_base(%struct.D* %this, i32 %x) {
entry:
; CHECK-LABEL: D_ctor_base:</pre>
<p>The use of <code>CHECK-LABEL:</code> directives in this case ensures that the three <code>CHECK:</code> directives only accept lines corresponding to the body of the <code>@C_ctor_base</code> function, even if the patterns match lines found later in the file. Furthermore, if one of these three <code>CHECK:</code> directives fail, FileCheck will recover by continuing to the next block, allowing multiple test failures to be detected in a single invocation. </p>
<p> There is no requirement that <code>CHECK-LABEL:</code> directives contain strings that correspond to actual syntactic labels in a source or output language: they must simply uniquely match a single line in the file being verified. </p>
<p> <code>CHECK-LABEL:</code> directives cannot contain variable definitions or uses.</p>
<h3>Directive modifiers</h3>
<p>A directive modifier can be append to a directive by following the directive with <code>{&lt;modifier&gt;}</code> where the only supported value for <code>&lt;modifier&gt;</code> is <code>LITERAL</code>. </p>
<p> The <code>LITERAL</code> directive modifier can be used to perform a literal match. The modifier results in the directive not recognizing any syntax to perform regex matching, variable capture or any substitutions. This is useful when the text to match would require excessive escaping otherwise. For example, the following will perform literal matches rather than considering these as regular expressions: </p>
<pre>Input: [[[10, 20]], [[30, 40]]]
Output %r10: [[10, 20]]
Output %r10: [[30, 40]]
; CHECK{LITERAL}: [[[10, 20]], [[30, 40]]]
; CHECK-DAG{LITERAL}: [[30, 40]]
; CHECK-DAG{LITERAL}: [[10, 20]]</pre>
<h3>FileCheck Regex Matching Syntax</h3>
<p>All FileCheck directives take a pattern to match. For most uses of FileCheck, fixed string matching is perfectly sufficient. For some things, a more flexible form of matching is desired. To support this, FileCheck allows you to specify regular expressions in matching strings, surrounded by double braces: <code>&#123;&#123;yourregex}}</code>. FileCheck implements a POSIX regular expression matcher; it supports Extended POSIX regular expressions (ERE). Because we want to use fixed string matching for a majority of what we do, FileCheck has been designed to support mixing and matching fixed string matching with regular expressions. This allows you to write things like this: </p>
<pre>; CHECK: movhpd &#123;&#123;[0-9]+}}(%esp), &#123;&#123;%xmm[0-7]}}</pre>
<p>In this case, any offset from the ESP register will be allowed, and any xmm register will be allowed. </p>
<p> Because regular expressions are enclosed with double braces, they are visually distinct, and you don’t need to use escape characters within the double braces like you would in C. In the rare case that you want to match double braces explicitly from the input, you can use something ugly like <code>&#123;&#123;[}][}]}}</code> as your pattern. Or if you are using the repetition count syntax, for example <code>[[:xdigit:]]{8}</code> to match exactly 8 hex digits, you would need to add parentheses like this <code>&#123;&#123;([[:xdigit:]]{8})}}</code> to avoid confusion with FileCheck’s closing double-brace.</p>
<h3>FileCheck String Substitution Blocks</h3>
<p>It is often useful to match a pattern and then verify that it occurs again later in the file. For codegen tests, this can be useful to allow any register, but verify that that register is used consistently later. To do this, <code>FileCheck</code> supports string substitution blocks that allow string variables to be defined and substituted into patterns. Here is a simple example: </p>
<pre>; CHECK: test5:
; CHECK: notw [[REGISTER:%[a-z]+]]
; CHECK: andw &#123;&#123;.*}}[[REGISTER]]</pre>
<p>The first check line matches a regex <code>%[a-z]+</code> and captures it into the string variable <code>REGISTER</code>. The second line verifies that whatever is in <code>REGISTER</code> occurs later in the file after an “<code>andw</code>”. <code>FileCheck</code> string substitution blocks are always contained in <code>[[ ]]</code> pairs, and string variable names can be formed with the regex <code>[a-zA-Z_][a-zA-Z0-9_]*</code>. If a colon follows the name, then it is a definition of the variable; otherwise, it is a substitution. </p>
<p> <code>FileCheck</code> variables can be defined multiple times, and substitutions always get the latest value. Variables can also be substituted later on the same line they were defined on. For example: </p>
<pre>; CHECK: op [[REG:r[0-9]+]], [[REG]]</pre>
<p>Can be useful if you want the operands of <code>op</code> to be the same register, and don’t care exactly which register it is. </p>
<p> If <code>&#8211;enable-var-scope</code> is in effect, variables with names that start with <code>$</code> are considered to be global. All others variables are local. All local variables get undefined at the beginning of each CHECK-LABEL block. Global variables are not affected by CHECK-LABEL. This makes it easier to ensure that individual tests are not affected by variables set in preceding tests.</p>
<h3>FileCheck Numeric Substitution Blocks</h3>
<p><code>FileCheck</code> also supports numeric substitution blocks that allow defining numeric variables and checking for numeric values that satisfy a numeric expression constraint based on those variables via a numeric substitution. This allows <code>CHECK:</code> directives to verify a numeric relation between two numbers, such as the need for consecutive registers to be used. </p>
<p> The syntax to capture a numeric value is <code>[[#%&lt;fmtspec&gt;,&lt;NUMVAR&gt;:]]</code> where:</p>
<dl>
<dt>&bull;</p>
<dd><code>%&lt;fmtspec&gt;,</code> is an optional format specifier to indicate what number format to match and the minimum number of digits to expect.</p>
<dt>&bull;</p>
<dd><code>&lt;NUMVAR&gt;:</code> is an optional definition of variable <code>&lt;NUMVAR&gt;</code> from the captured value. </p>
<p> The syntax of <code>&lt;fmtspec&gt;</code> is: <code>#.&lt;precision&gt;&lt;conversion specifier&gt;</code> where:</p>
<dt>&bull;</p>
<dd><code>#</code> is an optional flag available for hex values (see <code>&lt;conversion specifier&gt;</code> below) which requires the value matched to be prefixed by <code>0x</code>.</p>
<dt>&bull;</p>
<dd><code>.&lt;precision&gt;</code> is an optional printf-style precision specifier in which <code>&lt;precision&gt;</code> indicates the minimum number of digits that the value matched must have, expecting leading zeros if needed.</p>
<dt>&bull;</p>
<dd><code>&lt;conversion specifier&gt;</code> is an optional scanf-style conversion specifier to indicate what number format to match (e.g. hex number). Currently accepted format specifiers are <code>%u</code>, <code>%d</code>, <code>%x</code> and <code>%X</code>. If absent, the format specifier defaults to <code>%u</code>. </p>
<p> For example: </p>
<pre>; CHECK: mov r[[#REG:]], 0x[[#%.8X,ADDR:]]</pre>
<p>would match <code>mov r5, 0x0000FEFE</code> and set <code>REG</code> to the value <code>5</code> and <code>ADDR</code> to the value <code>0xFEFE</code>. Note that due to the precision it would fail to match <code>mov r5, 0xFEFE</code>. </p>
<p> As a result of the numeric variable definition being optional, it is possible to only check that a numeric value is present in a given format. This can be useful when the value itself is not useful, for instance: </p>
<pre>; CHECK-NOT: mov r0, r[[#]]</pre>
<p>to check that a value is synthesized rather than moved around. </p>
<p> The syntax of a numeric substitution is <code>[[#%&lt;fmtspec&gt;, &lt;constraint&gt; &lt;expr&gt;]]</code> where:</p>
<dt>&bull;</p>
<dd><code>&lt;fmtspec&gt;</code> is the same format specifier as for defining a variable but in this context indicating how a numeric expression value should be matched against. If absent, both components of the format specifier are inferred from the matching format of the numeric variable(s) used by the expression constraint if any, and defaults to <code>%u</code> if no numeric variable is used, denoting that the value should be unsigned with no leading zeros. In case of conflict between format specifiers of several numeric variables, the conversion specifier becomes mandatory but the precision specifier remains optional.</p>
<dt>&bull;</p>
<dd><code>&lt;constraint&gt;</code> is the constraint describing how the value to match must relate to the value of the numeric expression. The only currently accepted constraint is <code>==</code> for an exact match and is the default if <code>&lt;constraint&gt;</code> is not provided. No matching constraint must be specified when the <code>&lt;expr&gt;</code> is empty.</p>
<dt>&bull;</p>
<dd><code>&lt;expr&gt;</code> is an expression. An expression is in turn recursively defined as:</p>
<dt>&bull;</p>
<dd>a numeric operand, or</p>
<dt>&bull;</p>
<dd>an expression followed by an operator and a numeric operand. </p>
<p> A numeric operand is a previously defined numeric variable, an integer literal, or a function. Spaces are accepted before, after and between any of these elements. Numeric operands have 64-bit precision. Overflow and underflow are rejected. There is no support for operator precedence, but parentheses can be used to change the evaluation order. </p>
<p> The supported operators are:</p>
<dt>&bull;</p>
<dd><code>+</code> &#8211; Returns the sum of its two operands.</p>
<dt>&bull;</p>
<dd><code>&#8211;</code> &#8211; Returns the difference of its two operands. </p>
<p> The syntax of a function call is <code>&lt;name&gt;(&lt;arguments&gt;)</code> where:</p>
<dt>&bull;</p>
<dd><code>name</code> is a predefined string literal. Accepted values are:</p>
<dt>&bull;</p>
<dd>add &#8211; Returns the sum of its two operands.</p>
<dt>&bull;</p>
<dd>div &#8211; Returns the quotient of its two operands.</p>
<dt>&bull;</p>
<dd>max &#8211; Returns the largest of its two operands.</p>
<dt>&bull;</p>
<dd>min &#8211; Returns the smallest of its two operands.</p>
<dt>&bull;</p>
<dd>mul &#8211; Returns the product of its two operands.</p>
<dt>&bull;</p>
<dd>sub &#8211; Returns the difference of its two operands.</p>
<dt>&bull;</p>
<dd><code>&lt;arguments&gt;</code> is a comma separated list of expressions. </p>
<p> For example: </p>
<pre>; CHECK: load r[[#REG:]], [r0]
; CHECK: load r[[#REG+1]], [r1]
; CHECK: Loading from 0x[[#%x,ADDR:]]
; CHECK-SAME: to 0x[[#ADDR + 7]]</pre>
<p>The above example would match the text: </p>
<pre>load r5, [r0]
load r6, [r1]
Loading from 0xa0463440 to 0xa0463447</pre>
<p>but would not match the text: </p>
<pre>load r5, [r0]
load r7, [r1]
Loading from 0xa0463440 to 0xa0463443</pre>
<p>Due to <code>7</code> being unequal to <code>5 + 1</code> and <code>a0463443</code> being unequal to <code>a0463440 + 7</code>. </p>
<p> A numeric variable can also be defined to the result of a numeric expression, in which case the numeric expression constraint is checked and if verified the variable is assigned to the value. The unified syntax for both checking a numeric expression and capturing its value into a numeric variable is thus <code>[[#%&lt;fmtspec&gt;,&lt;NUMVAR&gt;: &lt;constraint&gt; &lt;expr&gt;]]</code> with each element as described previously. One can use this syntax to make a testcase more self-describing by using variables instead of values: </p>
<pre>; CHECK: mov r[[#REG_OFFSET:]], 0x[[#%X,FIELD_OFFSET:12]]
; CHECK-NEXT: load r[[#]], [r[[#REG_BASE:]], r[[#REG_OFFSET]]]</pre>
<p>which would match: </p>
<pre>mov r4, 0xC
load r6, [r5, r4]</pre>
<p>The <code>&#8211;enable-var-scope</code> option has the same effect on numeric variables as on string variables. </p>
<p> Important note: In its current implementation, an expression cannot use a numeric variable defined earlier in the same CHECK directive.</dl>
<h3>FileCheck Pseudo Numeric Variables</h3>
<p>Sometimes there’s a need to verify output that contains line numbers of the match file, e.g. when testing compiler diagnostics. This introduces a certain fragility of the match file structure, as “<code>CHECK:</code>” lines contain absolute line numbers in the same file, which have to be updated whenever line numbers change due to text addition or deletion. </p>
<p> To support this case, FileCheck expressions understand the <code>@LINE</code> pseudo numeric variable which evaluates to the line number of the CHECK pattern where it is found. </p>
<p> This way match patterns can be put near the relevant test lines and include relative line number references, for example: </p>
<pre>// CHECK: test.cpp:[[# @LINE + 4]]:6: error: expected ';' after top level declarator
// CHECK-NEXT: &#123;&#123;^int a}}
// CHECK-NEXT: &#123;&#123;^ \^}}
// CHECK-NEXT: &#123;&#123;^ ;}}
int a</pre>
<p>To support legacy uses of <code>@LINE</code> as a special string variable, <code>FileCheck</code> also accepts the following uses of <code>@LINE</code> with string substitution block syntax: <code>[[@LINE]]</code>, <code>[[@LINE+&lt;offset&gt;]]</code> and <code>[[@LINE-&lt;offset&gt;]]</code> without any spaces inside the brackets and where <code>offset</code> is an integer.</p>
<h3>Matching Newline Characters</h3>
<p>To match newline characters in regular expressions the character class <code>[[:space:]]</code> can be used. For example, the following pattern: </p>
<pre>// CHECK: DW_AT_location [DW_FORM_sec_offset] ([[DLOC:0x[0-9a-f]+]])&#123;&#123;[[:space:]].*}}&quot;intd&quot;</pre>
<p>matches output of the form (from llvm-dwarfdump): </p>
<pre>DW_AT_location [DW_FORM_sec_offset] (0x00000233)
DW_AT_name [DW_FORM_strp] ( .debug_str[0x000000c9] = &quot;intd&quot;)</pre>
<p>letting us set the <code>FileCheck</code> variable <code>DLOC</code> to the desired value <code>0x00000233</code>, extracted from the line immediately preceding “<code>intd</code>”.</p>
<h2>Author</h2>
<p>Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>Copyright</h2>
<p>2003-2022, LLVM Project</p>
