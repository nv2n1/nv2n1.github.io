---
title: "go-testfunc(7)"
name: "go-testfunc"
section: "7"
letter: "g"
url: "/docs/linux/man/7-go-testfunc/"
---

go - tool for managing Go source code

<h2>Description</h2>

The 'go test' command expects to find test, benchmark, and example functions in the &quot;*_test.go&quot; files corresponding to the package under test. A test function is one named TestXxx (where Xxx does not start with a lower case letter) and should have the signature, <pre> func TestXxx(t *testing.T) { ... }</pre>A benchmark function is one named BenchmarkXxx and should have the signature, <pre> func BenchmarkXxx(b *testing.B) { ... }</pre>An example function is similar to a test function but, instead of using *testing.T to report success or failure, prints output to os.Stdout. If the last comment in the function starts with &quot;Output:&quot; then the output is compared exactly against the comment (see examples below). If the last comment begins with &quot;Unordered output:&quot; then the output is compared to the comment, however the order of the lines is ignored. An example with no such comment is compiled but not executed. An example with no text after &quot;Output:&quot; is compiled, executed, and expected to produce no output. Godoc displays the body of ExampleXxx to demonstrate the use of the function, constant, or variable Xxx. An example of a method M with receiver type T or *T is named ExampleT_M. There may be multiple examples for a given function, constant, or variable, distinguished by a trailing _xxx, where xxx is a suffix not beginning with an upper case letter. Here is an example of an example: <pre> func ExamplePrintln() {
 Println(&quot;The output of\nthis example.&quot;)
 // Output: The output of
 // this example.
 }</pre>Here is another example where the ordering of the output is ignored: <pre><code>func ExamplePerm()
{
          for
              _, value : = range Perm(4)
              {
                  fmt.Println(value)
              }

          // Unordered output: 4
          // 2
          // 1
          // 3
          // 0
}</code></pre> The entire test file is presented as the example when it contains a single example function, at least one other function, type, variable, or constant declaration, and no test or benchmark functions. See the documentation of the testing package for more information.

<h2>Author</h2>

This manual page was written by Michael Stapelberg &lt;stapelberg [at] debian.org&gt; and is maintained by the Debian Go Compiler Team &lt;team+go-compiler [at] tracker.debian.org&gt; based on the output of 'go help testfunc' for the Debian project (and may be used by others).
