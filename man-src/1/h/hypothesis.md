---
title: "hypothesis(1)"
name: "hypothesis"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hypothesis/"
---

<h2>NAME</h2>

 hypothesis - Hypothesis Documentation 

 <i>Hypothesis</i> is a Python library for creating unit tests which are simpler to write and more powerful when run, finding edge cases in your code you wouldn't have thought to look for. It is stable, powerful and easy to add to any existing test suite. 

 It works by letting you write tests that assert that something should be true for every case, not just the ones you happen to think of. 

 Think of a normal unit test as being something like the following:
<dl>
<dt>1.
<dd> Set up some data.
<dt>2.
<dd> Perform some operations on the data.
<dt>3.
<dd> Assert something about the result. 

 Hypothesis lets you write tests which instead look like this:
<dt>1.
<dd> For all data matching some specification.
<dt>2.
<dd> Perform some operations on the data.
<dt>3.
<dd> Assert something about the result. 

 This is often called property based testing, and was popularised by the Haskell library <i>Quickcheck</i>. 

 It works by generating random data matching your specification and checking that your guarantee still holds in that case. If it finds an example where it doesn't, it takes that example and cuts it down to size, simplifying it until it finds a much smaller example that still causes the problem. It then saves that example for later, so that once it has found a problem with your code it will not forget it in the future. 

 Writing tests of this form usually consists of deciding on guarantees that your code should make - properties that should always hold true, regardless of what the world throws at you. Examples of such guarantees might be:
<dt>&bull;
<dd> Your code shouldn't throw an exception, or should only throw a particular type of exception (this works particularly well if you have a lot of internal assertions).
<dt>&bull;
<dd> If you delete an object, it is no longer visible.
<dt>&bull;
<dd> If you serialize and then deserialize a value, then you get the same value back. 

 Now you know the basics of what Hypothesis does, the rest of this documentation will take you through how and why. It's divided into a number of sections, which you can see in the sidebar (or the menu at the top if you're on mobile), but you probably want to begin with the <b>Quick start guide</b>, which will give you a worked example of how to use Hypothesis and a detailed outline of the things you need to know to begin testing your code with it, or check out some of the <i>introductory articles</i>.</dl>

<h2>QUICK START GUIDE</h2>

 

 This document should talk you through everything you need to get started with Hypothesis.

<h3>An example</h3>

 

 Suppose we've written a <i>run length encoding</i> system and we want to test it out. 

 We have the following code which I took straight from the <i>Rosetta Code</i> wiki (OK, I removed some commented out code and fixed the formatting, but there are no functional modifications): 

 <pre>
def encode(input_string):
    count = 1
    prev = ''
    lst = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev, count)
                lst.append(entry)
            count = 1
            prev = character
        else:
            count += 1
    else:
        entry = (character, count)
        lst.append(entry)
    return lst
def decode(lst):
    q = ''
    for character, count in lst:
        q += character * count
    return q
</pre> 

 We want to write a test for this that will check some invariant of these functions. 

 The invariant one tends to try when you've got this sort of encoding / decoding is that if you encode something and then decode it then you get the same value back. 

 Lets see how you'd do that with Hypothesis: 

 <pre>
from hypothesis import given
from hypothesis.strategies import text
@given(text())
def test_decode_inverts_encode(s):
    assert decode(encode(s)) == s
</pre> 

 (For this example we'll just let pytest discover and run the test. We'll cover other ways you could have run it later). 

 The text function returns what Hypothesis calls a search strategy. An object with methods that describe how to generate and simplify certain kinds of values. The @given decorator then takes our test function and turns it into a parametrized one which, when called, will run the test function over a wide range of matching data from that strategy. 

 Anyway, this test immediately finds a bug in the code: 

 <pre>
Falsifying example: test_decode_inverts_encode(s='')
UnboundLocalError: local variable 'character' referenced before assignment
</pre> 

 Hypothesis correctly points out that this code is simply wrong if called on an empty string. 

 If we fix that by just adding the following code to the beginning of the function then Hypothesis tells us the code is correct (by doing nothing as you'd expect a passing test to). 

 <pre>
if not input_string:
    return []
</pre> 

 If we wanted to make sure this example was always checked we could add it in explicitly: 

 <pre>
from hypothesis import given, example
from hypothesis.strategies import text
@given(text())
@example('')
def test_decode_inverts_encode(s):
    assert decode(encode(s)) == s
</pre> 

 You don't have to do this, but it can be useful both for clarity purposes and for reliably hitting hard to find examples. Also in local development Hypothesis will just remember and reuse the examples anyway, but there's not currently a very good workflow for sharing those in your CI. 

 It's also worth noting that both example and given support keyword arguments as well as positional. The following would have worked just as well: 

 <pre>
@given(s=text())
@example(s='')
def test_decode_inverts_encode(s):
    assert decode(encode(s)) == s
</pre> 

 Suppose we had a more interesting bug and forgot to reset the count each time. Say we missed a line in our <b>encode</b> method: 

 <pre>
def encode(input_string):
  count = 1
  prev = ''
  lst = []
  for character in input_string:
      if character != prev:
          if prev:
              entry = (prev, count)
              lst.append(entry)
          # count = 1  # Missing reset operation
          prev = character
      else:
          count += 1
  else:
      entry = (character, count)
      lst.append(entry)
  return lst
</pre> 

 Hypothesis quickly informs us of the following example: 

 <pre>
Falsifying example: test_decode_inverts_encode(s='001')
</pre> 

 Note that the example provided is really quite simple. Hypothesis doesn't just find <i>any</i> counter-example to your tests, it knows how to simplify the examples it finds to produce small easy to understand ones. In this case, two identical values are enough to set the count to a number different from one, followed by another distinct value which should have reset the count but in this case didn't. 

 The examples Hypothesis provides are valid Python code you can run. Any arguments that you explicitly provide when calling the function are not generated by Hypothesis, and if you explicitly provide <i>all</i> the arguments Hypothesis will just call the underlying function the once rather than running it multiple times.

<h3>Installing</h3>

 

 Hypothesis is <i>available on pypi as &quot;hypothesis&quot;</i>. You can install it with: 

 <pre>
pip install hypothesis
</pre> 

 If you want to install directly from the source code (e.g. because you want to make changes and install the changed version) you can do this with: 

 <pre>
pip install -e .
</pre> 

 You should probably run the tests first to make sure nothing is broken. You can do this with: 

 <pre>
python setup.py test
</pre> 

 Note that if they're not already installed this will try to install the test dependencies. 

 You may wish to do all of this in a <i>virtualenv</i>. For example: 

 <pre>
virtualenv venv
source venv/bin/activate
pip install hypothesis
</pre> 

 Will create an isolated environment for you to try hypothesis out in without affecting your system installed packages.

<h3>Running tests</h3>

 

 In our example above we just let pytest discover and run our tests, but we could also have run it explicitly ourselves: 

 <pre>
if __name__ == '__main__':
    test_decode_inverts_encode()
</pre> 

 We could also have done this as a unittest TestCase: 

 <pre>
import unittest
class TestEncoding(unittest.TestCase):
    @given(text())
    def test_decode_inverts_encode(self, s):
        self.assertEqual(decode(encode(s)), s)
if __name__ == '__main__':
    unittest.main()
</pre> 

 A detail: This works because Hypothesis ignores any arguments it hasn't been told to provide (positional arguments start from the right), so the self argument to the test is simply ignored and works as normal. This also means that Hypothesis will play nicely with other ways of parameterizing tests. e.g it works fine if you use pytest fixtures for some arguments and Hypothesis for others.

<h3>Writing tests</h3>

 

 A test in Hypothesis consists of two parts: A function that looks like a normal test in your test framework of choice but with some additional arguments, and a <b>@given</b> decorator that specifies how to provide those arguments. 

 Here are some other examples of how you could use that: 

 <pre>
from hypothesis import given
import hypothesis.strategies as st
@given(st.integers(), st.integers())
def test_ints_are_commutative(x, y):
    assert x + y == y + x
@given(x=st.integers(), y=st.integers())
def test_ints_cancel(x, y):
    assert (x + y) - y == x
@given(st.lists(st.integers()))
def test_reversing_twice_gives_same_list(xs):
    # This will generate lists of arbitrary length (usually between 0 and
    # 100 elements) whose elements are integers.
    ys = list(xs)
    ys.reverse()
    ys.reverse()
    assert xs == ys
@given(st.tuples(st.booleans(), st.text()))
def test_look_tuples_work_too(t):
    # A tuple is generated as the one you provided, with the corresponding
    # types in those positions.
    assert len(t) == 2
    assert isinstance(t[0], bool)
    assert isinstance(t[1], str)
</pre> 

 Note that as we saw in the above example you can pass arguments to <b>@given</b> either as positional or as keywords.

<h3>Where to start</h3>

 

 You should now know enough of the basics to write some tests for your code using Hypothesis. The best way to learn is by doing, so go have a try. 

 If you're stuck for ideas for how to use this sort of test for your code, here are some good starting points:
<dl>
<dt>1.
<dd> Try just calling functions with appropriate random data and see if they crash. You may be surprised how often this works. e.g. note that the first bug we found in the encoding example didn't even get as far as our assertion: It crashed because it couldn't handle the data we gave it, not because it did the wrong thing.
<dt>2.
<dd> Look for duplication in your tests. Are there any cases where you're testing the same thing with multiple different examples? Can you generalise that to a single test using Hypothesis?
<dt>3.
<dd> <i>This piece is designed for an F# implementation</i>, but is still very good advice which you may find helps give you good ideas for using Hypothesis. 

 If you have any trouble getting started, don't feel shy about <b>asking for help</b>.</dl>

<h2>DETAILS AND ADVANCED FEATURES</h2>

 

 This is an account of slightly less common Hypothesis features that you don't need to get started but will nevertheless make your life easier.

<h3>Additional test output</h3>

 

 Normally the output of a failing test will look something like: 

 <pre>
Falsifying example: test_a_thing(x=1, y=&quot;foo&quot;)
</pre> 

 With the <b>repr</b> of each keyword argument being printed. 

 Sometimes this isn't enough, either because you have values with a <b>repr</b> that isn't very descriptive or because you need to see the output of some intermediate steps of your test. That's where the <b>note</b> function comes in: 

 <pre>
&gt;&gt;&gt; from hypothesis import given, note, strategies as st
&gt;&gt;&gt; @given(st.lists(st.integers()), st.randoms())
... def test_shuffle_is_noop(ls, r):
...     ls2 = list(ls)
...     r.shuffle(ls2)
...     note(&quot;Shuffle: %r&quot; % (ls2))
...     assert ls == ls2
...
&gt;&gt;&gt; try:
...     test_shuffle_is_noop()
... except AssertionError:
...     print('ls != ls2')
Falsifying example: test_shuffle_is_noop(ls=[0, 0, 1], r=RandomWithSeed(0))
Shuffle: [0, 1, 0]
ls != ls2
</pre> 

 The note is printed in the final run of the test in order to include any additional information you might need in your test.

<h3>Test Statistics</h3>

 

 If you are using py.test you can see a number of statistics about the executed tests by passing the command line argument <b>--hypothesis-show-statistics</b>. This will include some general statistics about the test: 

 For example if you ran the following with <b>--hypothesis-show-statistics</b>: 

 <pre>
from hypothesis import given, strategies as st
@given(st.integers())
def test_integers(i):
    pass
</pre> 

 You would see: 

 <pre>
test_integers:
  - 200 passing examples, 0 failing examples, 0 invalid examples
  - Typical runtimes: &lt; 1ms
  - Stopped because settings.max_examples=200
</pre> 

 The final &quot;Stopped because&quot; line is particularly important to note: It tells you the setting value that determined when the test should stop trying new examples. This can be useful for understanding the behaviour of your tests. Ideally you'd always want this to be max_examples. 

 In some cases (such as filtered and recursive strategies) you will see events mentioned which describe some aspect of the data generation: 

 <pre>
from hypothesis import given, strategies as st
@given(st.integers().filter(lambda x: x % 2 == 0))
def test_even_integers(i):
    pass
</pre> 

 You would see something like: 

 <pre>
test_even_integers:
  - 200 passing examples, 0 failing examples, 16 invalid examples
  - Typical runtimes: &lt; 1ms
  - Stopped because settings.max_examples=200
  - Events:
    * 30.56%, Retried draw from integers().filter(lambda x: x % 2 == 0) to satisfy filter
    * 7.41%, Aborted test because unable to satisfy integers().filter(lambda x: x % 2 == 0)
</pre>
<dl>
<dt><b>hypothesis.event(value)</b>
<dd> Record an event that occurred this test. Statistics on number of test runs with each event will be reported at the end if you run Hypothesis in statistics reporting mode. 

 Events should be strings or convertable to them. 

 You can also mark custom events in a test using the 'event' function: 

 <pre>
from hypothesis import given, event, strategies as st
@given(st.integers().filter(lambda x: x % 2 == 0))
def test_even_integers(i):
    event(&quot;i mod 3 = %d&quot; % (i % 3,))
</pre> 

 You will then see output like: 

 <pre>
test_even_integers:
  - 200 passing examples, 0 failing examples, 28 invalid examples
  - Typical runtimes: &lt; 1ms
  - Stopped because settings.max_examples=200
  - Events:
    * 47.81%, Retried draw from integers().filter(lambda x: x % 2 == 0) to satisfy filter
    * 31.14%, i mod 3 = 2
    * 28.95%, i mod 3 = 1
    * 27.63%, i mod 3 = 0
    * 12.28%, Aborted test because unable to satisfy integers().filter(lambda x: x % 2 == 0)
</pre> 

 Arguments to event() can be any hashable type, but two events will be considered the same if they are the same when converted to a string with str().</dl>

<h3>Making assumptions</h3>

 

 Sometimes Hypothesis doesn't give you exactly the right sort of data you want - it's mostly of the right shape, but some examples won't work and you don't want to care about them. You <i>can</i> just ignore these by aborting the test early, but this runs the risk of accidentally testing a lot less than you think you are. Also it would be nice to spend less time on bad examples - if you're running 200 examples per test (the default) and it turns out 150 of those examples don't match your needs, that's a lot of wasted time.
<dl>
<dt><b>hypothesis.assume(condition)</b>
<dd> <b>assume()</b> is like an <i>assert</i> that marks the example as bad, rather than failing the test. 

 This allows you to specify properties that you <i>assume</i> will be true, and let Hypothesis try to avoid similar examples in future. 

 For example suppose had the following test: 

 <pre>
@given(floats())
def test_negation_is_self_inverse(x):
    assert x == -(-x)
</pre> 

 Running this gives us: 

 <pre>
Falsifying example: test_negation_is_self_inverse(x=float('nan'))
AssertionError
</pre> 

 This is annoying. We know about NaN and don't really care about it, but as soon as Hypothesis finds a NaN example it will get distracted by that and tell us about it. Also the test will fail and we want it to pass. 

 So lets block off this particular example: 

 <pre>
from math import isnan
@given(floats())
def test_negation_is_self_inverse_for_non_nan(x):
    assume(not isnan(x))
    assert x == -(-x)
</pre> 

 And this passes without a problem. 

 In order to avoid the easy trap where you assume a lot more than you intended, Hypothesis will fail a test when it can't find enough examples passing the assumption. 

 If we'd written: 

 <pre>
@given(floats())
def test_negation_is_self_inverse_for_non_nan(x):
    assume(False)
    assert x == -(-x)
</pre> 

 Then on running we'd have got the exception: 

 <pre>
Unsatisfiable: Unable to satisfy assumptions of hypothesis test_negation_is_self_inverse_for_non_nan. Only 0 examples considered satisfied assumptions
</pre></dl>

<h3>How good is assume?</h3>

 

 Hypothesis has an adaptive exploration strategy to try to avoid things which falsify assumptions, which should generally result in it still being able to find examples in hard to find situations. 

 Suppose we had the following: 

 <pre>
@given(lists(integers()))
def test_sum_is_positive(xs):
  assert sum(xs) &gt; 0
</pre> 

 Unsurprisingly this fails and gives the falsifying example []. 

 Adding <b>assume(xs)</b> to this removes the trivial empty example and gives us [0]. 

 Adding <b>assume(all(x &gt; 0 for x in xs))</b> and it passes: A sum of a list of positive integers is positive. 

 The reason that this should be surprising is not that it doesn't find a counter-example, but that it finds enough examples at all. 

 In order to make sure something interesting is happening, suppose we wanted to try this for long lists. e.g. suppose we added an assume(len(xs) &gt; 10) to it. This should basically never find an example: A naive strategy would find fewer than one in a thousand examples, because if each element of the list is negative with probability half, you'd have to have ten of these go the right way by chance. In the default configuration Hypothesis gives up long before it's tried 1000 examples (by default it tries 200). 

 Here's what happens if we try to run this: 

 <pre>
@given(lists(integers()))
def test_sum_is_positive(xs):
    assume(len(xs) &gt; 10)
    assume(all(x &gt; 0 for x in xs))
    print(xs)
    assert sum(xs) &gt; 0
In: test_sum_is_positive()
[17, 12, 7, 13, 11, 3, 6, 9, 8, 11, 47, 27, 1, 31, 1]
[6, 2, 29, 30, 25, 34, 19, 15, 50, 16, 10, 3, 16]
[25, 17, 9, 19, 15, 2, 2, 4, 22, 10, 10, 27, 3, 1, 14, 17, 13, 8, 16, 9, 2...
[17, 65, 78, 1, 8, 29, 2, 79, 28, 18, 39]
[13, 26, 8, 3, 4, 76, 6, 14, 20, 27, 21, 32, 14, 42, 9, 24, 33, 9, 5, 15, ...
[2, 1, 2, 2, 3, 10, 12, 11, 21, 11, 1, 16]
</pre> 

 As you can see, Hypothesis doesn't find <i>many</i> examples here, but it finds some - enough to keep it happy. 

 In general if you <i>can</i> shape your strategies better to your tests you should - for example <b>integers(1, 1000)</b> is a lot better than <b>assume(1 &lt;= x &lt;= 1000)</b>, but assume will take you a long way if you can't.

<h3>Defining strategies</h3>

 

 The type of object that is used to explore the examples given to your test function is called a <b>SearchStrategy</b>. These are created using the functions exposed in the <b>hypothesis.strategies</b> module. 

 Many of these strategies expose a variety of arguments you can use to customize generation. For example for integers you can specify <b>min</b> and <b>max</b> values of integers you want. If you want to see exactly what a strategy produces you can ask for an example: 

 <pre>
&gt;&gt;&gt; integers(min_value=0, max_value=10).example()
5
</pre> 

 Many strategies are build out of other strategies. For example, if you want to define a tuple you need to say what goes in each element: 

 <pre>
&gt;&gt;&gt; from hypothesis.strategies import tuples
&gt;&gt;&gt; tuples(integers(), integers()).example()
(50, 15)
</pre> 

 Further details are <b>available in a separate document</b>.

<h3>The gory details of given parameters</h3>

<dl>
<dt><b>hypothesis.given(*given_arguments, **given_kwargs)</b>
<dd> A decorator for turning a test function that accepts arguments into a randomized test. 

 This is the main entry point to Hypothesis. 

 The <b>@given</b> decorator may be used to specify what arguments of a function should be parametrized over. You can use either positional or keyword arguments or a mixture of the two. 

 For example all of the following are valid uses: 

 <pre>
@given(integers(), integers())
def a(x, y):
  pass
@given(integers())
def b(x, y):
  pass
@given(y=integers())
def c(x, y):
  pass
@given(x=integers())
def d(x, y):
  pass
@given(x=integers(), y=integers())
def e(x, **kwargs):
  pass
@given(x=integers(), y=integers())
def f(x, *args, **kwargs):
  pass
class SomeTest(TestCase):
    @given(integers())
    def test_a_thing(self, x):
        pass
</pre> 

 The following are not: 

 <pre>
@given(integers(), integers(), integers())
def g(x, y):
    pass
@given(integers())
def h(x, *args):
    pass
@given(integers(), x=integers())
def i(x, y):
    pass
@given()
def j(x, y):
    pass
</pre> 

 The rules for determining what are valid uses of given are as follows:
<dt>1.
<dd> You may pass any keyword argument to given.
<dt>2.
<dd> Positional arguments to given are equivalent to the rightmost named arguments for the test function.
<dt>3.
<dd> positional arguments may not be used if the underlying test function has varargs or arbitrary keywords.
<dt>4.
<dd> Functions tested with given may not have any defaults. 

 The reason for the &quot;rightmost named arguments&quot; behaviour is so that using <b>@given</b> with instance methods works: <b>self</b> will be passed to the function as normal and not be parametrized over. 

 The function returned by given has all the arguments that the original test did , minus the ones that are being filled in by given.</dl>

<h3>Custom function execution</h3>

 

 Hypothesis provides you with a hook that lets you control how it runs examples. 

 This lets you do things like set up and tear down around each example, run examples in a subprocess, transform coroutine tests into normal tests, etc. 

 The way this works is by introducing the concept of an executor. An executor is essentially a function that takes a block of code and run it. The default executor is: 

 <pre>
def default_executor(function):
    return function()
</pre> 

 You define executors by defining a method execute_example on a class. Any test methods on that class with <b>@given</b> used on them will use <b>self.execute_example</b> as an executor with which to run tests. For example, the following executor runs all its code twice: 

 <pre>
from unittest import TestCase
class TestTryReallyHard(TestCase):
    @given(integers())
    def test_something(self, i):
        perform_some_unreliable_operation(i)
    def execute_example(self, f):
        f()
        return f()
</pre> 

 Note: The functions you use in map, etc. will run <i>inside</i> the executor. i.e. they will not be called until you invoke the function passed to setup_example. 

 An executor must be able to handle being passed a function which returns None, otherwise it won't be able to run normal test cases. So for example the following executor is invalid: 

 <pre>
from unittest import TestCase
class TestRunTwice(TestCase):
    def execute_example(self, f):
        return f()()
</pre> 

 and should be rewritten as: 

 <pre>
from unittest import TestCase
import inspect
class TestRunTwice(TestCase):
    def execute_example(self, f):
        result = f()
        if inspect.isfunction(result):
            result = result()
        return result
</pre>

<h3>Using Hypothesis to find values</h3>

 

 You can use Hypothesis's data exploration features to find values satisfying some predicate. This is generally useful for exploring custom strategies defined with <b>@composite</b>, or experimenting with conditions for filtering data.
<dl>
<dt><b>hypothesis.find(specifier, condition, settings=None, random=None, database_key=None)</b>
<dd> Returns the minimal example from the given strategy <b>specifier</b> that matches the predicate function <b>condition</b>. 

 <pre>
&gt;&gt;&gt; from hypothesis import find
&gt;&gt;&gt; from hypothesis.strategies import sets, lists, integers
&gt;&gt;&gt; find(lists(integers()), lambda x: sum(x) &gt;= 10)
[10]
&gt;&gt;&gt; find(lists(integers()), lambda x: sum(x) &gt;= 10 and len(x) &gt;= 3)
[0, 0, 10]
&gt;&gt;&gt; find(sets(integers()), lambda x: sum(x) &gt;= 10 and len(x) &gt;= 3)
{0, 1, 9}
</pre> 

 The first argument to <b>find()</b> describes data in the usual way for an argument to given, and supports <b>all the same data types</b>. The second is a predicate it must satisfy. 

 Of course not all conditions are satisfiable. If you ask Hypothesis for an example to a condition that is always false it will raise an error: 

 <pre>
&gt;&gt;&gt; find(integers(), lambda x: False)
Traceback (most recent call last):
...
hypothesis.errors.NoSuchExample: No examples of condition lambda x: &lt;unknown&gt;
</pre> 

 (The <b>lambda x: unknown</b> is because Hypothesis can't retrieve the source code of lambdas from the interactive python console. It gives a better error message most of the time which contains the actual condition)</dl>

<h3>Providing explicit examples</h3>

 

 You can explicitly ask Hypothesis to try a particular example, using
<dl>
<dt><b>hypothesis.example(*args, **kwargs)</b>
<dd> A decorator to that ensures a specific example is always tested. 

 Hypothesis will run all examples you've asked for first. If any of them fail it will not go on to look for more examples. 

 It doesn't matter whether you put the example decorator before or after given. Any permutation of the decorators in the above will do the same thing. 

 Note that examples can be positional or keyword based. If they're positional then they will be filled in from the right when calling, so either of the following styles will work as expected: 

 <pre>
@given(text())
@example(&quot;Hello world&quot;)
@example(x=&quot;Some very long string&quot;)
def test_some_code(x):
    assert True
from unittest import TestCase
class TestThings(TestCase):
    @given(text())
    @example(&quot;Hello world&quot;)
    @example(x=&quot;Some very long string&quot;)
    def test_some_code(self, x):
        assert True
</pre> 

 It is <i>not</i> permitted for a single example to be a mix of positional and keyword arguments. Either are fine, and you can use one in one example and the other in another example if for some reason you really want to, but a single example must be consistent.</dl>

<h2>SETTINGS</h2>

 

 Hypothesis tries to have good defaults for its behaviour, but sometimes that's not enough and you need to tweak it. 

 The mechanism for doing this is the <b>settings</b> object. You can set up a @given based test to use this using a settings decorator: 

 <b>@given</b> invocation as follows: 

 <pre>
from hypothesis import given, settings
@given(integers())
@settings(max_examples=500)
def test_this_thoroughly(x):
    pass
</pre> 

 This uses a <b>settings</b> object which causes the test to receive a much larger set of examples than normal. 

 This may be applied either before or after the given and the results are the same. The following is exactly equivalent: 

 <pre>
from hypothesis import given, settings
@settings(max_examples=500)
@given(integers())
def test_this_thoroughly(x):
    pass
</pre>

<h3>Available settings</h3>

<dl>
<dt><b>class hypothesis.settings(parent=None, **kwargs)</b>
<dd> A settings object controls a variety of parameters that are used in falsification. These may control both the falsification strategy and the details of the data that is generated. 

 Default values are picked up from the settings.default object and changes made there will be picked up in newly created settings.
<dt><b>database_file</b>
<dd> database: An instance of hypothesis.database.ExampleDatabase that will be used to save examples to and load previous examples from. May be None in which case no storage will be used. default value: (dynamically calculated)
<dt><b>database</b>
<dd> An ExampleDatabase instance to use for storage of examples. May be None. 

 If this was explicitly set at settings instantiation then that value will be used (even if it was None). If not and the database_file setting is not None this will be lazily loaded as an ExampleDatabase using that file the first time this property is accessed on a particular thread.
<dt><b>max_examples</b>
<dd> Once this many satisfying examples have been considered without finding any counter-example, falsification will terminate. default value: 200
<dt><b>max_iterations</b>
<dd> Once this many iterations of the example loop have run, including ones which failed to satisfy assumptions and ones which produced duplicates, falsification will terminate. default value: 1000
<dt><b>min_satisfying_examples</b>
<dd> Raise Unsatisfiable for any tests which do not produce at least this many values that pass all assume() calls and which have not exhaustively covered the search space. default value: 5
<dt><b>max_shrinks</b>
<dd> Once this many successful shrinks have been performed, Hypothesis will assume something has gone a bit wrong and give up rather than continuing to try to shrink the example. default value: 500
<dt><b>timeout</b>
<dd> Once this many seconds have passed, falsify will terminate even if it has not found many examples. This is a soft rather than a hard limit - Hypothesis won't e.g. interrupt execution of the called function to stop it. If this value is &lt;= 0 then no timeout will be applied. default value: 60
<dt><b>strict</b>
<dd> If set to True, anything that would cause Hypothesis to issue a warning will instead raise an error. Note that new warnings may be added at any time, so running with strict set to True means that new Hypothesis releases may validly break your code. 

 You can enable this setting temporarily by setting the HYPOTHESIS_STRICT_MODE environment variable to the string 'true'. default value: False
<dt><b>stateful_step_count</b>
<dd> Number of steps to run a stateful program for before giving up on it breaking. default value: 50
<dt><b>perform_health_check</b>
<dd> If set to True, Hypothesis will run a preliminary health check before attempting to actually execute your test. default value: True
<dt><b>suppress_health_check</b>
<dd> A list of health checks to disable default value: []
<dt><b>buffer_size</b>
<dd> The size of the underlying data used to generate examples. If you need to generate really large examples you may want to increase this, but it will make your tests slower. default value: 8192</dl>

<h3>Seeing intermediate result</h3>

 

 To see what's going on while Hypothesis runs your tests, you can turn up the verbosity setting. This works with both <b>find()</b> and <b>@given</b>. 

 <pre>
&gt;&gt;&gt; from hypothesis import find, settings, Verbosity
&gt;&gt;&gt; from hypothesis.strategies import lists, booleans
&gt;&gt;&gt; find(lists(integers()), any, settings=settings(verbosity=Verbosity.verbose))
Found satisfying example [-208]
Shrunk example to [-208]
Shrunk example to [208]
Shrunk example to [1]
[1]
</pre> 

 The four levels are quiet, normal, verbose and debug. normal is the default, while in quiet Hypothesis will not print anything out, even the final falsifying example. debug is basically verbose but a bit more so. You probably don't want it. 

 You can also override the default by setting the environment variable <b>HYPOTHESIS_VERBOSITY_LEVEL</b> to the name of the level you want. So e.g. setting <b>HYPOTHESIS_VERBOSITY_LEVEL=verbose</b> will run all your tests printing intermediate results and errors.

<h3>Building settings objects</h3>

 

 settings can be created by calling settings with any of the available settings values. Any absent ones will be set to defaults: 

 <pre>
&gt;&gt;&gt; from hypothesis import settings
&gt;&gt;&gt; settings()  
settings(buffer_size=8192, database_file='...', derandomize=False,
         max_examples=200, max_iterations=1000, max_mutations=10,
         max_shrinks=500, min_satisfying_examples=5, perform_health_check=True,
         phases=..., report_statistics=..., stateful_step_count=50, strict=...,
         suppress_health_check=[], timeout=60, verbosity=Verbosity.normal)
&gt;&gt;&gt; settings().max_examples
200
&gt;&gt;&gt; settings(max_examples=10).max_examples
10
</pre> 

 You can also copy settings off other settings: 

 <pre>
&gt;&gt;&gt; s = settings(max_examples=10)
&gt;&gt;&gt; t = settings(s, max_iterations=20)
&gt;&gt;&gt; s.max_examples
10
&gt;&gt;&gt; t.max_iterations
20
&gt;&gt;&gt; s.max_iterations
1000
&gt;&gt;&gt; s.max_shrinks
500
&gt;&gt;&gt; t.max_shrinks
500
</pre>

<h3>Default settings</h3>

 

 At any given point in your program there is a current default settings, available as settings.default. As well as being a settings object in its own right, all newly created settings objects which are not explicitly based off another settings are based off the default, so will inherit any values that are not explicitly set from it. 

 You can change the defaults by using profiles (see next section), but you can also override them locally by using a settings object as a <i>context manager</i> 

 <pre>
&gt;&gt;&gt; with settings(max_examples=150):
...     print(settings.default.max_examples)
...     print(settings().max_examples)
150
150
&gt;&gt;&gt; settings().max_examples
200
</pre> 

 Note that after the block exits the default is returned to normal. 

 You can use this by nesting test definitions inside the context: 

 <pre>
from hypothesis import given, settings
with settings(max_examples=500):
    @given(integers())
    def test_this_thoroughly(x):
        pass
</pre> 

 All settings objects created or tests defined inside the block will inherit their defaults from the settings object used as the context. You can still override them with custom defined settings of course. 

 Warning: If you use define test functions which don't use @given inside a context block, these will not use the enclosing settings. This is because the context manager only affects the definition, not the execution of the function.

<h3>settings Profiles</h3>

 

 Depending on your environment you may want different default settings. For example: during development you may want to lower the number of examples to speed up the tests. However, in a CI environment you may want more examples so you are more likely to find bugs. 

 Hypothesis allows you to define different settings profiles. These profiles can be loaded at any time. 

 Loading a profile changes the default settings but will not change the behavior of tests that explicitly change the settings. 

 <pre>
&gt;&gt;&gt; from hypothesis import settings
&gt;&gt;&gt; settings.register_profile(&quot;ci&quot;, settings(max_examples=1000))
&gt;&gt;&gt; settings().max_examples
200
&gt;&gt;&gt; settings.load_profile(&quot;ci&quot;)
&gt;&gt;&gt; settings().max_examples
1000
</pre> 

 Instead of loading the profile and overriding the defaults you can retrieve profiles for specific tests. 

 <pre>
&gt;&gt;&gt; with settings.get_profile(&quot;ci&quot;):
...     print(settings().max_examples)
...
1000
</pre> 

 Optionally, you may define the environment variable to load a profile for you. This is the suggested pattern for running your tests on CI. The code below should run in a <i>conftest.py</i> or any setup/initialization section of your test suite. If this variable is not defined the Hypothesis defined defaults will be loaded. 

 <pre>
&gt;&gt;&gt; import os
&gt;&gt;&gt; from hypothesis import settings
&gt;&gt;&gt; settings.register_profile(&quot;ci&quot;, settings(max_examples=1000))
&gt;&gt;&gt; settings.register_profile(&quot;dev&quot;, settings(max_examples=10))
&gt;&gt;&gt; settings.register_profile(&quot;debug&quot;, settings(max_examples=10, verbosity=Verbosity.verbose))
&gt;&gt;&gt; settings.load_profile(os.getenv(u'HYPOTHESIS_PROFILE', 'default'))
</pre> 

 If you are using the hypothesis pytest plugin and your profiles are registered by your conftest you can load one with the command line option <b>--hypothesis-profile</b>. 

 <pre>
$ py.test tests --hypothesis-profile &lt;profile-name&gt;
</pre>

<h2>WHAT YOU CAN GENERATE AND HOW</h2>

 

 The general philosophy of Hypothesis data generation is that everything should be possible to generate and most things should be easy. Most things in the standard library is more aspirational than achieved, the state of the art is already pretty good. 

 This document is a guide to what strategies are available for generating data and how to build them. Strategies have a variety of other important internal features, such as how they simplify, but the data they can generate is the only public part of their API. 

 Functions for building strategies are all available in the hypothesis.strategies module. The salient functions from it are as follows:
<dl>
<dt><b>hypothesis.strategies.nothing()</b>
<dd> This strategy never successfully draws a value and will always reject on an attempt to draw.
<dt><b>hypothesis.strategies.just(value)</b>
<dd> Return a strategy which only generates value. 

 Note: value is not copied. Be wary of using mutable values.
<dt><b>hypothesis.strategies.none()</b>
<dd> Return a strategy which only generates None.
<dt><b>hypothesis.strategies.one_of(*args)</b>
<dd> Return a strategy which generates values from any of the argument strategies. 

 This may be called with one iterable argument instead of multiple strategy arguments. In which case one_of(x) and one_of(*x) are equivalent.
<dt><b>hypothesis.strategies.integers(min_value=None, max_value=None)</b>
<dd> Returns a strategy which generates integers (in Python 2 these may be ints or longs). 

 If min_value is not None then all values will be &gt;= min_value. If max_value is not None then all values will be &lt;= max_value
<dt><b>hypothesis.strategies.booleans()</b>
<dd> Returns a strategy which generates instances of bool.
<dt><b>hypothesis.strategies.floats(min_value=None, max_value=None, allow_nan=None, allow_infinity=None)</b>
<dd> Returns a strategy which generates floats.
<dt>&bull;
<dd> If min_value is not None, all values will be &gt;= min_value.
<dt>&bull;
<dd> If max_value is not None, all values will be &lt;= max_value.
<dt>&bull;
<dd> If min_value or max_value is not None, it is an error to enable allow_nan.
<dt>&bull;
<dd> If both min_value and max_value are not None, it is an error to enable allow_infinity. 

 Where not explicitly ruled out by the bounds, all of infinity, -infinity and NaN are possible values generated by this strategy.
<dt><b>hypothesis.strategies.complex_numbers()</b>
<dd> Returns a strategy that generates complex numbers.
<dt><b>hypothesis.strategies.tuples(*args)</b>
<dd> Return a strategy which generates a tuple of the same length as args by generating the value at index i from args[i]. 

 e.g. tuples(integers(), integers()) would generate a tuple of length two with both values an integer.
<dt><b>hypothesis.strategies.sampled_from(elements)</b>
<dd> Returns a strategy which generates any value present in the iterable elements. 

 Note that as with just, values will not be copied and thus you should be careful of using mutable data.
<dt><b>hypothesis.strategies.lists(elements=None, min_size=None, average_size=None, max_size=None, unique_by=None, unique=False)</b>
<dd> Returns a list containing values drawn from elements length in the interval [min_size, max_size] (no bounds in that direction if these are None). If max_size is 0 then elements may be None and only the empty list will be drawn. 

 average_size may be used as a size hint to roughly control the size of list but it may not be the actual average of sizes you get, due to a variety of factors. 

 If unique is True (or something that evaluates to True), we compare direct object equality, as if unique_by was <i>lambda x: x</i>. This comparison only works for hashable types. 

 if unique_by is not None it must be a function returning a hashable type when given a value drawn from elements. The resulting list will satisfy the condition that for i != j, unique_by(result[i]) != unique_by(result[j]).
<dt><b>hypothesis.strategies.sets(elements=None, min_size=None, average_size=None, max_size=None)</b>
<dd> This has the same behaviour as lists, but returns sets instead. 

 Note that Hypothesis cannot tell if values are drawn from elements are hashable until running the test, so you can define a strategy for sets of an unhashable type but it will fail at test time.
<dt><b>hypothesis.strategies.frozensets(elements=None, min_size=None, average_size=None, max_size=None)</b>
<dd> This is identical to the sets function but instead returns frozensets.
<dt><b>hypothesis.strategies.iterables(elements=None, min_size=None, average_size=None, max_size=None, unique_by=None, unique=False)</b>
<dd> This has the same behaviour as lists, but returns iterables instead. 

 Some iterables cannot be indexed (e.g. sets) and some do not have a fixed length (e.g. generators). This strategy produces iterators, which cannot be indexed and do not have a fixed length. This ensures that you do not accidentally depend on sequence behaviour.
<dt><b>hypothesis.strategies.fixed_dictionaries(mapping)</b>
<dd> Generate a dictionary of the same type as mapping with a fixed set of keys mapping to strategies. mapping must be a dict subclass. 

 Generated values have all keys present in mapping, with the corresponding values drawn from mapping[key]. If mapping is an instance of OrderedDict the keys will also be in the same order, otherwise the order is arbitrary.
<dt><b>hypothesis.strategies.dictionaries(keys, values, dict_class=&lt;type 'dict'&gt;, min_size=None, average_size=None, max_size=None)</b>
<dd> Generates dictionaries of type dict_class with keys drawn from the keys argument and values drawn from the values argument. 

 The size parameters have the same interpretation as for lists.
<dt><b>hypothesis.strategies.streaming(elements)</b>
<dd> Generates an infinite stream of values where each value is drawn from elements. 

 The result is iterable (the iterator will never terminate) and indexable.
<dt><b>hypothesis.strategies.characters(whitelist_categories=None, blacklist_categories=None, blacklist_characters=None, min_codepoint=None, max_codepoint=None)</b>
<dd> Generates unicode text type (unicode on python 2, str on python 3) characters following specified filtering rules. 

 This strategy accepts lists of Unicode categories, characters of which should (<i>whitelist_categories</i>) or should not (<i>blacklist_categories</i>) be produced. 

 Also there could be applied limitation by minimal and maximal produced code point of the characters. 

 If you know what exactly characters you don't want to be produced, pass them with <i>blacklist_characters</i> argument.
<dt><b>hypothesis.strategies.text(alphabet=None, min_size=None, average_size=None, max_size=None)</b>
<dd> Generates values of a unicode text type (unicode on python 2, str on python 3) with values drawn from alphabet, which should be an iterable of length one strings or a strategy generating such. If it is None it will default to generating the full unicode range. If it is an empty collection this will only generate empty strings. 

 min_size, max_size and average_size have the usual interpretations.
<dt><b>hypothesis.strategies.binary(min_size=None, average_size=None, max_size=None)</b>
<dd> Generates the appropriate binary type (str in python 2, bytes in python 3). 

 min_size, average_size and max_size have the usual interpretations.
<dt><b>hypothesis.strategies.randoms()</b>
<dd> Generates instances of Random (actually a Hypothesis specific RandomWithSeed class which displays what it was initially seeded with)
<dt><b>hypothesis.strategies.random_module()</b>
<dd> If your code depends on the global random module then you need to use this. 

 It will explicitly seed the random module at the start of your test so that tests are reproducible. The value it passes you is an opaque object whose only useful feature is that its repr displays the random seed. It is not itself a random number generator. If you want a random number generator you should use the randoms() strategy which will give you one.
<dt><b>hypothesis.strategies.builds(target, *args, **kwargs)</b>
<dd> Generates values by drawing from args and kwargs and passing them to target in the appropriate argument position. 

 e.g. builds(target, integers(), flag=booleans()) would draw an integer i and a boolean b and call target(i, flag=b).
<dt><b>hypothesis.strategies.fractions(min_value=None, max_value=None, max_denominator=None)</b>
<dd> Returns a strategy which generates Fractions. 

 If min_value is not None then all generated values are no less than min_value. 

 If max_value is not None then all generated values are no greater than max_value. 

 If max_denominator is not None then the absolute value of the denominator of any generated values is no greater than max_denominator. Note that max_denominator must be at least 1.
<dt><b>hypothesis.strategies.decimals(min_value=None, max_value=None, allow_nan=None, allow_infinity=None, places=None)</b>
<dd> Generates instances of decimals.Decimal, which may be:
<dt>&bull;
<dd> A finite rational number, between <b>min_value</b> and <b>max_value</b>.
<dt>&bull;
<dd> Not a Number, if <b>allow_nan</b> is True. None means &quot;allow NaN, unless <b>min__value</b> and <b>max_value</b> are not None&quot;.
<dt>&bull;
<dd> Positive or negative infinity, if <b>max_value</b> and <b>min_value</b> respectively are None, and <b>allow_infinity</b> is not False. None means &quot;allow infinity, unless excluded by the min and max values&quot;. 

 Note that where floats have one <i>NaN</i> value, Decimals have four: signed, and either <i>quiet</i> or <i>signalling</i>. See <i>the decimal module docs</i> for more information on special values. 

 If <b>places</b> is not None, all finite values drawn from the strategy will have that number of digits after the decimal place.
<dt><b>hypothesis.strategies.recursive(base, extend, max_leaves=100)</b>
<dd> base: A strategy to start from. 

 extend: A function which takes a strategy and returns a new strategy. 

 max_leaves: The maximum number of elements to be drawn from base on a given run. 

 This returns a strategy S such that S = extend(base | S). That is, values maybe drawn from base, or from any strategy reachable by mixing applications of | and extend. 

 An example may clarify: recursive(booleans(), lists) would return a strategy that may return arbitrarily nested and mixed lists of booleans. So e.g. False, [True], [False, []], [[[[True]]]], are all valid values to be drawn from that strategy.
<dt><b>hypothesis.strategies.permutations(values)</b>
<dd> Return a strategy which returns permutations of the collection &quot;values&quot;.
<dt><b>hypothesis.strategies.datetimes(min_datetime=datetime.datetime(1, 1, 1, 0, 0), max_datetime=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999), timezones=none())</b>
<dd> A strategy for generating datetimes, which may be timezone-aware. 

 This strategy works by drawing a naive datetime between <b>min_datetime</b> and <b>max_datetime</b>, which must both be naive (have no timezone). 

 <b>timezones</b> must be a strategy that generates tzinfo objects (or None, which is valid for naive datetimes). A value drawn from this strategy will be added to a naive datetime, and the resulting tz-aware datetime returned. 

 <b>NOTE:</b> tz-aware datetimes from this strategy may be ambiguous or non-existent due to daylight savings, leap seconds, timezone and calendar adjustments, etc. This is intentional, as malformed timestamps are a common source of bugs. 

 <b>hypothesis.extra.timezones()</b> requires the <b>pytz</b> package, but provides all timezones in the Olsen database. If you also want to allow naive datetimes, combine strategies like <b>none() | timezones()</b>. 

 Alternatively, you can create a list of the timezones you wish to allow (e.g. from the standard library, <b>datetutil</b>, or <b>pytz</b>) and use <b>sampled_from()</b>. Ensure that simple values such as None or UTC are at the beginning of the list for proper minimisation.
<dt><b>hypothesis.strategies.dates(min_date=datetime.date(1, 1, 1), max_date=datetime.date(9999, 12, 31))</b>
<dd> A strategy for dates between <b>min_date</b> and <b>max_date</b>.
<dt><b>hypothesis.strategies.times(min_time=datetime.time(0, 0), max_time=datetime.time(23, 59, 59, 999999), timezones=none())</b>
<dd> A strategy for times between <b>min_time</b> and <b>max_time</b>. 

 The <b>timezones</b> argument is handled as for <b>datetimes()</b>.
<dt><b>hypothesis.strategies.timedeltas(min_delta=datetime.timedelta(-999999999), max_delta=datetime.timedelta(999999999, 86399, 999999))</b>
<dd> A strategy for timedeltas between <b>min_delta</b> and <b>max_delta</b>.
<dt><b>hypothesis.strategies.composite(f)</b>
<dd> Defines a strategy that is built out of potentially arbitrarily many other strategies. 

 This is intended to be used as a decorator. See <i>the full documentation for more details</i> about how to use this function.
<dt><b>hypothesis.strategies.shared(base, key=None)</b>
<dd> Returns a strategy that draws a single shared value per run, drawn from base. Any two shared instances with the same key will share the same value, otherwise the identity of this strategy will be used. That is: 

 <pre>
&gt;&gt;&gt; s = integers()  # or any other strategy
&gt;&gt;&gt; x = shared(s)
&gt;&gt;&gt; y = shared(s)
</pre> 

 In the above x and y may draw different (or potentially the same) values. In the following they will always draw the same: 

 <pre>
&gt;&gt;&gt; x = shared(s, key=&quot;hi&quot;)
&gt;&gt;&gt; y = shared(s, key=&quot;hi&quot;)
</pre>
<dt><b>hypothesis.strategies.choices()</b>
<dd> Strategy that generates a function that behaves like random.choice. 

 Will note choices made for reproducibility.
<dt><b>hypothesis.strategies.uuids()</b>
<dd> Returns a strategy that generates UUIDs. 

 All returned values from this will be unique, so e.g. if you do lists(uuids()) the resulting list will never contain duplicates.
<dt><b>hypothesis.strategies.runner(default=not_set)</b>
<dd> A strategy for getting &quot;the current test runner&quot;, whatever that may be. The exact meaning depends on the entry point, but it will usually be the associated 'self' value for it. 

 If there is no current test runner and a default is provided, return that default. If no default is provided, raises InvalidArgument.
<dt><b>hypothesis.strategies.data()</b>
<dd> This isn't really a normal strategy, but instead gives you an object which can be used to draw data interactively from other strategies. 

 It can only be used within <b>@given</b>, not <b>find()</b>. This is because the lifetime of the object cannot outlast the test body. 

 See <i>the rest of the documentation</i> for more complete information.</dl>

<h3>Choices</h3>

 

 Sometimes you need an input to be from a known set of items. Hypothesis gives you two ways to do this. First up, <b>choice()</b>: 

 <pre>
from hypothesis import given, strategies as st
@given(user=st.text(min_size=1), service=st.text(min_size=1), choice=st.choices())
def test_tickets(user, service, choice):
    t=choice(('ST', 'LT', 'TG', 'CT'))
    # asserts go here.
</pre> 

 This means <b>t</b> will randomly be one of the items in the list ('ST', 'LT', 'TG', 'CT'), as if you were calling <b>python:random.choice()</b> on the list. 

 A different, and probably better way to do this, is to use <b>sampled_from()</b>: 

 <pre>
from hypothesis import given, strategies as st
@given(
    user=st.text(min_size=1), service=st.text(min_size=1),
    t=st.sampled_from(('ST', 'LT', 'TG', 'CT')))
def test_tickets(user, service, t):
    # asserts and test code go here.
</pre> 

 Values from <b>sampled_from()</b> will not be copied and thus you should be careful of using mutable data. This is great for the above use case, but may not always work out.

<h3>Infinite streams</h3>

 

 Sometimes you need examples of a particular type to keep your test going but you're not sure how many you'll need in advance. For this, we have streaming types. 

 <pre>
&gt;&gt;&gt; from hypothesis.types import Stream
&gt;&gt;&gt; x = Stream(iter(integers().example, None))
&gt;&gt;&gt; # Equivalent to `streaming(integers()).example()`, which is not supported
&gt;&gt;&gt; x  
Stream(...)
&gt;&gt;&gt; x[2]
131
&gt;&gt;&gt; x  
Stream(-225, 50, 131, ...)
&gt;&gt;&gt; x[10]
127
&gt;&gt;&gt; x  
Stream(-225, 50, 131, 30781241791694610923869406150329382725, 89, 62248, 107, 35771, -113, 79, 127, ...)
</pre> 

 Think of a Stream as an infinite list where we've only evaluated as much as we need to. As per above, you can index into it and the stream will be evaluated up to that index and no further. 

 You can iterate over it too (warning: iter on a stream given to you by Hypothesis in this way will never terminate): 

 <pre>
&gt;&gt;&gt; it = iter(x)
&gt;&gt;&gt; next(it)
-225
&gt;&gt;&gt; next(it)
50
&gt;&gt;&gt; next(it)
131
</pre> 

 Slicing will also work, and will give you back Streams. If you set an upper bound then iter on those streams <i>will</i> terminate: 

 <pre>
&gt;&gt;&gt; list(x[:5])
[-225, 50, 131, 30781241791694610923869406150329382725, 89]
&gt;&gt;&gt; y = x[1::2]
&gt;&gt;&gt; y  
Stream(...)
&gt;&gt;&gt; y[0]
50
&gt;&gt;&gt; y[1]
30781241791694610923869406150329382725
&gt;&gt;&gt; y  
Stream(50, 30781241791694610923869406150329382725, ...)
</pre> 

 You can also apply a function to transform a stream: 

 <pre>
&gt;&gt;&gt; t = x[20:]
&gt;&gt;&gt; tm = t.map(lambda n: n * 2)
&gt;&gt;&gt; tm[0]
-344
&gt;&gt;&gt; t[0]
-172
&gt;&gt;&gt; tm  
Stream(-344, ...)
&gt;&gt;&gt; t  
Stream(-172, ...)
</pre> 

 map creates a new stream where each element of the stream is the function applied to the corresponding element of the original stream. Evaluating the new stream will force evaluating the original stream up to that index. 

 (Warning: This isn't the map builtin. In Python 3 the builtin map should do more or less the right thing, but in Python 2 it will never terminate and will just eat up all your memory as it tries to build an infinitely long list) 

 These are the only operations a Stream supports. There are a few more internal ones, but you shouldn't rely on them.

<h3>Adapting strategies</h3>

 

 Often it is the case that a strategy doesn't produce exactly what you want it to and you need to adapt it. Sometimes you can do this in the test, but this hurts reuse because you then have to repeat the adaption in every test. 

 Hypothesis gives you ways to build strategies from other strategies given functions for transforming the data.

<h3>Mapping</h3>

 

 Map is probably the easiest and most useful of these to use. If you have a strategy <b>s</b> and a function <b>f</b>, then an example <b>s.map(f).example()</b> is <b>f(s.example())</b>, i.e. we draw an example from <b>s</b> and then apply <b>f</b> to it. 

 e.g.: 

 <pre>
&gt;&gt;&gt; lists(integers()).map(sorted).example()
[-224, -222, 16, 159, 120699286316048]
</pre> 

 Note that many things that you might use mapping for can also be done with <b>hypothesis.strategies.builds()</b>.

<h3>Filtering</h3>

 

 filter lets you reject some examples. <b>s.filter(f).example()</b> is some example of <b>s</b> such that <b>f(example)</b> is truthy. 

 <pre>
&gt;&gt;&gt; integers().filter(lambda x: x &gt; 11).example()
1609027033942695427531
&gt;&gt;&gt; integers().filter(lambda x: x &gt; 11).example()
251
</pre> 

 It's important to note that filter isn't magic and if your condition is too hard to satisfy then this can fail: 

 <pre>
&gt;&gt;&gt; integers().filter(lambda x: False).example()
Traceback (most recent call last):
  ...
hypothesis.errors.NoExamples: Could not find any valid examples in 20 tries
</pre> 

 In general you should try to use filter only to avoid corner cases that you don't want rather than attempting to cut out a large chunk of the search space. 

 A technique that often works well here is to use map to first transform the data and then use filter to remove things that didn't work out. So for example if you wanted pairs of integers (x,y) such that x &lt; y you could do the following: 

 <pre>
&gt;&gt;&gt; tuples(integers(), integers()).map(
... lambda x: tuple(sorted(x))).filter(lambda x: x[0] != x[1]).example()
(180, 241)
</pre>

<h3>Chaining strategies together</h3>

 

 Finally there is flatmap. Flatmap draws an example, then turns that example into a strategy, then draws an example from <i>that</i> strategy. 

 It may not be obvious why you want this at first, but it turns out to be quite useful because it lets you generate different types of data with relationships to eachother. 

 For example suppose we wanted to generate a list of lists of the same length: 

 <pre>
&gt;&gt;&gt; rectangle_lists = integers(min_value=0, max_value=10).flatmap(
... lambda n: lists(lists(integers(), min_size=n, max_size=n)))
&gt;&gt;&gt; find(rectangle_lists, lambda x: True)
[]
&gt;&gt;&gt; find(rectangle_lists, lambda x: len(x) &gt;= 10)
[[], [], [], [], [], [], [], [], [], []]
&gt;&gt;&gt; find(rectangle_lists, lambda t: len(t) &gt;= 3 and len(t[0]) &gt;= 3)
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
&gt;&gt;&gt; find(rectangle_lists, lambda t: sum(len(s) for s in t) &gt;= 10)
[[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]
</pre> 

 In this example we first choose a length for our tuples, then we build a strategy which generates lists containing lists precisely of that length. The finds show what simple examples for this look like. 

 Most of the time you probably don't want flatmap, but unlike filter and map which are just conveniences for things you could just do in your tests, flatmap allows genuinely new data generation that you wouldn't otherwise be able to easily do. 

 (If you know Haskell: Yes, this is more or less a monadic bind. If you don't know Haskell, ignore everything in these parentheses. You do not need to understand anything about monads to use this, or anything else in Hypothesis).

<h3>Recursive data</h3>

 

 Sometimes the data you want to generate has a recursive definition. e.g. if you wanted to generate JSON data, valid JSON is:
<dl>
<dt>1.
<dd> Any float, any boolean, any unicode string.
<dt>2.
<dd> Any list of valid JSON data
<dt>3.
<dd> Any dictionary mapping unicode strings to valid JSON data. 

 The problem is that you cannot call a strategy recursively and expect it to not just blow up and eat all your memory. The other problem here is that not all unicode strings display consistently on different machines, so we'll restrict them in our doctest. 

 The way Hypothesis handles this is with the <b>recursive()</b> function which you pass in a base case and a function that given a strategy for your data type returns a new strategy for it. So for example: 

 <pre>
&gt;&gt;&gt; from string import printable; from pprint import pprint
&gt;&gt;&gt; json = recursive(none() | booleans() | floats() | text(printable),
... lambda children: lists(children) | dictionaries(text(printable), children))
&gt;&gt;&gt; pprint(json.example())
{'': 'Me$',
 &quot;\r5qPZ%etF:vL'9gC&quot;: False,
 '$KsT(( J/(wQ': [],
 '0)G&amp;31': False,
 '7': [],
 'C.i]A-I': {':?Xh&gt;[;': None,
             'YHT\r!\x0b': -6.801160220000663e+18,
...
&gt;&gt;&gt; pprint(json.example())
[{&quot;7_8'qyb&quot;: None,
  ':': -0.3641507440748771,
  'TI_^\n&gt;L{T\x0c': -0.0,
  'ZiOqQ\t': 'RKT*a]IjI/Zx2HB4ODiSUN)LsZ',
  'n;E^^6|9=@g@@BmAi': '7j5\\'},
 True]
&gt;&gt;&gt; pprint(json.example())
[]
</pre> 

 That is, we start with our leaf data and then we augment it by allowing lists and dictionaries of anything we can generate as JSON data. 

 The size control of this works by limiting the maximum number of values that can be drawn from the base strategy. So for example if we wanted to only generate really small JSON we could do this as: 

 <pre>
&gt;&gt;&gt; small_lists = recursive(booleans(), lists, max_leaves=5)
&gt;&gt;&gt; small_lists.example()
True
&gt;&gt;&gt; small_lists.example()
[True, False]
&gt;&gt;&gt; small_lists.example()
True
</pre></dl>

<h3>Composite strategies</h3>

 

 The <b>@composite</b> decorator lets you combine other strategies in more or less arbitrary ways. It's probably the main thing you'll want to use for complicated custom strategies. 

 The composite decorator works by giving you a function as the first argument that you can use to draw examples from other strategies. For example, the following gives you a list and an index into it: 

 <pre>
&gt;&gt;&gt; @composite
... def list_and_index(draw, elements=integers()):
...     xs = draw(lists(elements, min_size=1))
...     i = draw(integers(min_value=0, max_value=len(xs) - 1))
...     return (xs, i)
</pre> 

 'draw(s)' is a function that should be thought of as returning s.example(), except that the result is reproducible and will minimize correctly. The decorated function has the initial argument removed from the list, but will accept all the others in the expected order. Defaults are preserved. 

 <pre>
&gt;&gt;&gt; list_and_index()
list_and_index()
&gt;&gt;&gt; list_and_index().example()
([215, 112], 0)
&gt;&gt;&gt; list_and_index(booleans())
list_and_index(elements=booleans())
&gt;&gt;&gt; list_and_index(booleans()).example()
([False, False], 1)
</pre> 

 Note that the repr will work exactly like it does for all the built-in strategies: It will be a function that you can call to get the strategy in question, with values provided only if they do not match the defaults. 

 You can use <b>assume</b> inside composite functions: 

 <pre>
@composite
def distinct_strings_with_common_characters(draw):
    x = draw(text(), min_size=1)
    y = draw(text(alphabet=x))
    assume(x != y)
    return (x, y)
</pre> 

 This works as assume normally would, filtering out any examples for which the passed in argument is falsey.

<h3>Drawing interactively in tests</h3>

 

 There is also the <b>data()</b> strategy, which gives you a means of using strategies interactively. Rather than having to specify everything up front in <b>@given</b> you can draw from strategies in the body of your test: 

 <pre>
@given(data())
def test_draw_sequentially(data):
    x = data.draw(integers())
    y = data.draw(integers(min_value=x))
    assert x &lt; y
</pre> 

 If the test fails, each draw will be printed with the falsifying example. e.g. the above is wrong (it has a boundary condition error), so will print: 

 <pre>
Falsifying example: test_draw_sequentially(data=data(...))
Draw 1: 0
Draw 2: 0
</pre> 

 As you can see, data drawn this way is simplified as usual. 

 Test functions using the <b>data()</b> strategy do not support explicit <b>@example(...)</b>s. In this case, the best option is usually to construct your data with <b>@composite</b> or the explicit example, and unpack this within the body of the test. 

 Optionally, you can provide a label to identify values generated by each call to <b>data.draw()</b>. These labels can be used to identify values in the output of a falsifying example. 

 For instance: 

 <pre>
@given(data())
def test_draw_sequentially(data):
    x = data.draw(integers(), label='First number')
    y = data.draw(integers(min_value=x), label='Second number')
    assert x &lt; y
</pre> 

 will produce the output: 

 <pre>
Falsifying example: test_draw_sequentially(data=data(...))
Draw 1 (First number): 0
Draw 2 (Second number): 0
</pre>

<h2>ADDITIONAL PACKAGES</h2>

 

 Hypothesis itself does not have any dependencies, but there are some packages that need additional things installed in order to work. 

 You can install these dependencies using the setuptools extra feature as e.g. <b>pip install hypothesis[django]</b>. This will check installation of compatible versions. 

 You can also just install hypothesis into a project using them, ignore the version constraints, and hope for the best. 

 In general &quot;Which version is Hypothesis compatible with?&quot; is a hard question to answer and even harder to regularly test. Hypothesis is always tested against the latest compatible version and each package will note the expected compatibility range. If you run into a bug with any of these please specify the dependency version.

<h3>hypothesis[pytz]</h3>

<h3>hypothesis[datetime]</h3>

<h3>hypothesis[fakefactory]</h3>

 

 <i>Fake-factory</i> is another Python library for data generation. hypothesis.extra.fakefactory is a package which lets you use fake-factory generators to parametrize tests. 

 The fake-factory API is extremely unstable, even between patch releases, and Hypothesis's support for it is unlikely to work with anything except the exact version it has been tested against. 

 hypothesis.extra.fakefactory defines a function fake_factory which returns a strategy for producing text data from any FakeFactory provider. 

 So for example the following will parametrize a test by an email address: 

 <pre>
&gt;&gt;&gt; fake_factory('email').example()
'tnader [at] prosacco.info'
&gt;&gt;&gt; fake_factory('name').example()
'ZbynÄk ÄernÃ½ CSc.'
</pre> 

 You can explicitly specify the locale (otherwise it uses any of the available locales), either as a single locale or as several: 

 <pre>
&gt;&gt;&gt; fake_factory('name', locale='en_GB').example()
'Antione Gerlach'
&gt;&gt;&gt; fake_factory('name', locales=['en_GB', 'cs_CZ']).example()
'MiloÅ¡ Å Å¥astnÃ½'
&gt;&gt;&gt; fake_factory('name', locales=['en_GB', 'cs_CZ']).example()
'Harm Sanford'
</pre> 

 If you want to your own FakeFactory providers you can do that too, passing them in as a providers argument: 

 <pre>
&gt;&gt;&gt; from faker.providers import BaseProvider
&gt;&gt;&gt; class KittenProvider(BaseProvider):
...     def meows(self):
...             return 'meow %d' % (self.random_number(digits=10),)
...
&gt;&gt;&gt; fake_factory('meows', providers=[KittenProvider]).example()
'meow 9139348419'
</pre> 

 Generally you probably shouldn't do this unless you're reusing a provider you already have - Hypothesis's facilities for strategy generation are much more powerful and easier to use. This is only here to provide easy reuse of things you already have.

<h3>hypothesis[django]</h3>

 

 hypothesis.extra.django adds support for testing your Django models with Hypothesis. 

 It is tested extensively against all versions of Django in mainstream or extended support, including LTS releases. It <i>may</i> be compatible with earlier versions too, but there's no support from us either and you really should update to get security patches. 

 It's large enough that it is <b>documented elsewhere</b>.

<h3>hypothesis[numpy]</h3>

 

 hypothesis.extra.numpy adds support for testing your Numpy code with Hypothesis. 

 This includes generating arrays, array shapes, and both scalar or compound dtypes. 

 Like the Django extra, <b>Numpy has it's own page</b>.

<h2>HYPOTHESIS FOR DJANGO USERS</h2>

 

 Hypothesis offers a number of features specific for Django testing, available in the <b>hypothesis[django]</b> <b>extra</b>. This is tested against each supported series with mainstream or extended support - if you're still getting security patches, you can test with Hypothesis. 

 Using it is quite straightforward: All you need to do is subclass <b>hypothesis.extra.django.TestCase</b> or <b>hypothesis.extra.django.TransactionTestCase</b> and you can use <b>@given</b> as normal, and the transactions will be per example rather than per test function as they would be if you used @given with a normal django test suite (this is important because your test function will be called multiple times and you don't want them to interfere with each other). Test cases on these classes that do not use <b>@given</b> will be run as normal. 

 I strongly recommend not using <b>TransactionTestCase</b> unless you really have to. Because Hypothesis runs this in a loop the performance problems it normally has are significantly exacerbated and your tests will be really slow. 

 In addition to the above, Hypothesis has some limited support for automatically deriving strategies for your model types, which you can then customize further. 

 <b>WARNING:</b> Hypothesis creates saved models. This will run inside your testing transaction when using the test runner, but if you use the dev console this will leave debris in your database. 

 For example, using the trivial django project I have for testing: 

 <pre>
&gt;&gt;&gt; from hypothesis.extra.django.models import models
&gt;&gt;&gt; from toystore.models import Customer
&gt;&gt;&gt; c = models(Customer).example()
&gt;&gt;&gt; c
&lt;Customer: Customer object&gt;
&gt;&gt;&gt; c.email
'jaime.urbina [at] gmail.com'
&gt;&gt;&gt; c.name
'\U00109d3d\U000e07be\U000165f8\U0003fabf\U000c12cd\U000f1910\U00059f12\U000519b0\U0003fabf\U000f1910\U000423fb\U000423fb\U00059f12\U000e07be\U000c12cd\U000e07be\U000519b0\U000165f8\U0003fabf\U0007bc31'
&gt;&gt;&gt; c.age
-873375803
</pre> 

 Hypothesis has just created this with whatever the relevant type of data is. 

 Obviously the customer's age is implausible, so lets fix that: 

 <pre>
&gt;&gt;&gt; from hypothesis.strategies import integers
&gt;&gt;&gt; c = models(Customer, age=integers(min_value=0, max_value=120)).example()
&gt;&gt;&gt; c
&lt;Customer: Customer object&gt;
&gt;&gt;&gt; c.age
5
</pre> 

 You can use this to override any fields you like. Sometimes this will be mandatory: If you have a non-nullable field of a type Hypothesis doesn't know how to create (e.g. a foreign key) then the models function will error unless you explicitly pass a strategy to use there. 

 Foreign keys are not automatically derived. If they're nullable they will default to always being null, otherwise you always have to specify them. e.g. suppose we had a Shop type with a foreign key to company, we would define a strategy for it as: 

 <pre>
shop_strategy = models(Shop, company=models(Company))
</pre>

<h3>Tips and tricks</h3>

<h3>Custom field types</h3>

 

 If you have a custom Django field type you can register it with Hypothesis's model deriving functionality by registering a default strategy for it: 

 <pre>
&gt;&gt;&gt; from toystore.models import CustomishField, Customish
&gt;&gt;&gt; models(Customish).example()
hypothesis.errors.InvalidArgument: Missing arguments for mandatory field
    customish for model Customish
&gt;&gt;&gt; from hypothesis.extra.django.models import add_default_field_mapping
&gt;&gt;&gt; from hypothesis.strategies import just
&gt;&gt;&gt; add_default_field_mapping(CustomishField, just(&quot;hi&quot;))
&gt;&gt;&gt; x = models(Customish).example()
&gt;&gt;&gt; x.customish
'hi'
</pre> 

 Note that this mapping is on exact type. Subtypes will not inherit it.

<h3>Generating child models</h3>

 

 For the moment there's no explicit support in hypothesis-django for generating dependent models. i.e. a Company model will generate no Shops. However if you want to generate some dependent models as well, you can emulate this by using the <i>flatmap</i> function as follows: 

 <pre>
from hypothesis.strategies import lists, just
def generate_with_shops(company):
  return lists(models(Shop, company=just(company))).map(lambda _: company)
company_with_shops_strategy = models(Company).flatmap(generate_with_shops)
</pre> 

 Lets unpack what this is doing: 

 The way flatmap works is that we draw a value from the original strategy, then apply a function to it which gives us a new strategy. We then draw a value from <i>that</i> strategy. So in this case we're first drawing a company, and then we're drawing a list of shops belonging to that company: The <i>just</i> strategy is a strategy such that drawing it always produces the individual value, so <b>models(Shop, company=just(company))</b> is a strategy that generates a Shop belonging to the original company. 

 So the following code would give us a list of shops all belonging to the same company: 

 <pre>
models(Company).flatmap(lambda c: lists(models(Shop, company=just(c))))
</pre> 

 The only difference from this and the above is that we want the company, not the shops. This is where the inner map comes in. We build the list of shops and then throw it away, instead returning the company we started for. This works because the models that Hypothesis generates are saved in the database, so we're essentially running the inner strategy purely for the side effect of creating those children in the database.

<h3>Using default field values</h3>

 

 Hypothesis ignores field defaults and always tries to generate values, even if it doesn't know how to. You can tell it to use the default value for a field instead of generating one by passing <b>fieldname=default_value</b> to <b>models()</b>: 

 <pre>
&gt;&gt;&gt; from toystore.models import DefaultCustomish
&gt;&gt;&gt; models(DefaultCustomish).example()
hypothesis.errors.InvalidArgument: Missing arguments for mandatory field
    customish for model DefaultCustomish
&gt;&gt;&gt; from hypothesis.extra.django.models import default_value
&gt;&gt;&gt; x = models(DefaultCustomish, customish=default_value).example()
&gt;&gt;&gt; x.customish
'b'
</pre>

<h2>SCIENTIFIC HYPOTHESIS (FOR NUMPY)</h2>

 

 Hypothesis offers a number of strategies for <i>NumPy</i> testing, available in the <b>hypothesis[numpy]</b> <b>extra</b>. It lives in the <b>hypothesis.extra.numpy</b> package. 

 The centerpiece is the <b>arrays</b> strategy, which generates arrays with any dtype, shape, and contents you can specify or give a strategy for. To make this as useful as possible, strategies are provided to generate array shapes and generate all kinds of fixed-size or compound dtypes.

<h2>HEALTH CHECKS</h2>

 

 Hypothesis tries to detect common mistakes and things that will cause difficulty at run time in the form of a number of 'health checks'. 

 These include detecting and warning about:
<dl>
<dt>&bull;
<dd> Strategies with very slow data generation
<dt>&bull;
<dd> Strategies which filter out too much
<dt>&bull;
<dd> Recursive strategies which branch too much
<dt>&bull;
<dd> Use of the global random module 

 If any of these scenarios are detected, Hypothesis will emit a warning about them. 

 The general goal of these health checks is to warn you about things that you are doing that might appear to work but will either cause Hypothesis to not work correctly or to perform badly. 

 To selectively disable health checks, use the suppress_health_check settings. The argument for this parameter is a list with elements drawn from any of the class-level attributes of the HealthCheck class. 

 To disable all health checks, set the perform_health_check settings parameter to False.</dl>

<h2>THE HYPOTHESIS EXAMPLE DATABASE</h2>

 

 When Hypothesis finds a bug it stores enough information in its database to reproduce it. This enables you to have a classic testing workflow of find a bug, fix a bug, and be confident that this is actually doing the right thing because Hypothesis will start by retrying the examples that broke things last time.

<h3>Limitations</h3>

 

 The database is best thought of as a cache that you never need to invalidate: Information may be lost when you upgrade a Hypothesis version or change your test, so you shouldn't rely on it for correctness - if there's an example you want to ensure occurs each time then <i>there's a feature for including them in your source code</i> - but it helps the development workflow considerably by making sure that the examples you've just found are reproduced.

<h3>File locations</h3>

 

 The default storage format is as a fairly opaque directory structure. Each test corresponds to a directory, and each example to a file within that directory. The standard location for it is .hypothesis/examples in your current working directory. You can override this, either by setting either the database_file property on a settings object (you probably want to specify it on settings.default) or by setting the HYPOTHESIS_DATABASE_FILE environment variable. 

 There is also a legacy sqlite3 based format. This is mostly still supported for compatibility reasons, and support will be dropped in some future version of Hypothesis. If you use a database file name ending in .db, .sqlite or .sqlite3 that format will be used instead.

<h3>Upgrading Hypothesis and changing your tests</h3>

 

 The design of the Hypothesis database is such that you can put arbitrary data in the database and not get wrong behaviour. When you upgrade Hypothesis, old data <i>might</i> be invalidated, but this should happen transparently. It should never be the case that e.g. changing the strategy that generates an argument sometimes gives you data from the old strategy.

<h3>Sharing your example database</h3>

 

 <b>NOTE:</b> If specific examples are important for correctness you should use the <b>@example</b> decorator, as the example database may discard entries due to changes in your code or dependencies. For most users, we therefore recommend using the example database locally and possibly persisting it between CI builds, but not tracking it under version control. 

 The examples database can be shared simply by checking the directory into version control, for example with the following <b>.gitignore</b>: 

 <pre>
# Ignore files cached by Hypothesis...
.hypothesis/
# except for the examples directory
!.hypothesis/examples/
</pre> 

 Like everything under <b>.hypothesis/</b>, the examples directory will be transparently created on demand. Unlike the other subdirectories, <b>examples/</b> is designed to handle merges, deletes, etc if you just add the directory into git, mercurial, or any similar version control system.

<h2>STATEFUL TESTING</h2>

 

 Hypothesis offers support for a stateful style of test, where instead of trying to produce a single data value that causes a specific test to fail, it tries to generate a program that errors. In many ways, this sort of testing is to classical property based testing as property based testing is to normal example based testing. 

 The idea doesn't originate with Hypothesis, though Hypothesis's implementation and approach is mostly not based on an existing implementation and should be considered some mix of novel and independent reinventions. 

 This style of testing is useful both for programs which involve some sort of mutable state and for complex APIs where there's no state per se but the actions you perform involve e.g. taking data from one function and feeding it into another. 

 The idea is that you teach Hypothesis how to interact with your program: Be it a server, a python API, whatever. All you need is to be able to answer the question &quot;Given what I've done so far, what could I do now?&quot;. After that, Hypothesis takes over and tries to find sequences of actions which cause a test failure. 

 Right now the stateful testing is a bit new and experimental and should be considered as a semi-public API: It may break between minor versions but won't break between patch releases, and there are still some rough edges in the API that will need to be filed off. 

 This shouldn't discourage you from using it. Although it's not as robust as the rest of Hypothesis, it's still pretty robust and more importantly is extremely powerful. I found a number of really subtle bugs in Hypothesis by turning the stateful testing onto a subset of the Hypothesis API, and you likely will find the same. 

 Enough preamble, lets see how to use it. 

 The first thing to note is that there are two levels of API: The low level but more flexible API and the higher level rule based API which is both easier to use and also produces a much better display of data due to its greater structure. We'll start with the more structured one.

<h3>Rule based state machines</h3>

 

 Rule based state machines are the ones you're most likely to want to use. They're significantly more user friendly and should be good enough for most things you'd want to do. 

 A rule based state machine is a collection of functions (possibly with side effects) which may depend on both values that Hypothesis can generate and also on values that have resulted from previous function calls. 

 You define a rule based state machine as follows: 

 <pre>
import unittest
from collections import namedtuple
from hypothesis import strategies as st
from hypothesis.stateful import RuleBasedStateMachine, Bundle, rule
Leaf = namedtuple('Leaf', ('label',))
Split = namedtuple('Split', ('left', 'right'))
class BalancedTrees(RuleBasedStateMachine):
    trees = Bundle('BinaryTree')
    @rule(target=trees, x=st.integers())
    def leaf(self, x):
        return Leaf(x)
    @rule(target=trees, left=trees, right=trees)
    def split(self, left, right):
        return Split(left, right)
    @rule(tree=trees)
    def check_balanced(self, tree):
        if isinstance(tree, Leaf):
            return
        else:
            assert abs(self.size(tree.left) - self.size(tree.right)) &lt;= 1
            self.check_balanced(tree.left)
            self.check_balanced(tree.right)
    def size(self, tree):
        if isinstance(tree, Leaf):
            return 1
        else:
            return 1 + self.size(tree.left) + self.size(tree.right)
</pre> 

 In this we declare a Bundle, which is a named collection of previously generated values. We define two rules which put data onto this bundle - one which just generates leaves with integer labels, the other of which takes two previously generated values and returns a new one. 

 We can then integrate this into our test suite by getting a unittest TestCase from it: 

 <pre>
TestTrees = BalancedTrees.TestCase
if __name__ == '__main__':
    unittest.main()
</pre> 

 (these will also be picked up by py.test if you prefer to use that). Running this we get: 

 <pre>
Step #1: v1 = leaf(x=0)
Step #2: v2 = split(left=v1, right=v1)
Step #3: v3 = split(left=v2, right=v1)
Step #4: check_balanced(tree=v3)
F
======================================================================
FAIL: runTest (hypothesis.stateful.BalancedTrees.TestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
(...)
assert abs(self.size(tree.left) - self.size(tree.right)) &lt;= 1
AssertionError
</pre> 

 Note how it's printed out a very short program that will demonstrate the problem. 

 ...the problem of course being that we've not actually written any code to balance this tree at <i>all</i>, so of course it's not balanced. 

 So lets balance some trees. 

 <pre>
from collections import namedtuple
from hypothesis import strategies as st
from hypothesis.stateful import RuleBasedStateMachine, Bundle, rule
Leaf = namedtuple('Leaf', ('label',))
Split = namedtuple('Split', ('left', 'right'))
class BalancedTrees(RuleBasedStateMachine):
    trees = Bundle('BinaryTree')
    balanced_trees = Bundle('balanced BinaryTree')
    @rule(target=trees, x=st.integers())
    def leaf(self, x):
        return Leaf(x)
    @rule(target=trees, left=trees, right=trees)
    def split(self, left, right):
        return Split(left, right)
    @rule(tree=balanced_trees)
    def check_balanced(self, tree):
        if isinstance(tree, Leaf):
            return
        else:
            assert abs(self.size(tree.left) - self.size(tree.right)) &lt;= 1, \
                repr(tree)
            self.check_balanced(tree.left)
            self.check_balanced(tree.right)
    @rule(target=balanced_trees, tree=trees)
    def balance_tree(self, tree):
        return self.split_leaves(self.flatten(tree))
    def size(self, tree):
        if isinstance(tree, Leaf):
            return 1
        else:
            return self.size(tree.left) + self.size(tree.right)
    def flatten(self, tree):
        if isinstance(tree, Leaf):
            return (tree.label,)
        else:
            return self.flatten(tree.left) + self.flatten(tree.right)
    def split_leaves(self, leaves):
        assert leaves
        if len(leaves) == 1:
            return Leaf(leaves[0])
        else:
            mid = len(leaves) // 2
            return Split(
                self.split_leaves(leaves[:mid]),
                self.split_leaves(leaves[mid:]),
            )
</pre> 

 We've now written a really noddy tree balancing implementation. This takes trees and puts them into a new bundle of data, and we only assert that things in the balanced_trees bundle are actually balanced. 

 If you run this it will sit there silently for a while (you can turn on <i>verbose output</i> to get slightly more information about what's happening. debug will give you all the intermediate programs being run) and then run, telling you your test has passed! Our balancing algorithm worked. 

 Now lets break it to make sure the test is still valid: 

 Changing the split to <b>mid = max(len(leaves) // 3, 1)</b> this should no longer balance, which gives us the following counter-example: 

 <pre>
v1 = leaf(x=0)
v2 = split(left=v1, right=v1)
v3 = balance_tree(tree=v1)
v4 = split(left=v2, right=v2)
v5 = balance_tree(tree=v4)
check_balanced(tree=v5)
</pre> 

 Note that the example could be shrunk further by deleting v3. Due to some technical limitations, Hypothesis was unable to find that particular shrink. In general it's rare for examples produced to be long, but they won't always be minimal. 

 You can control the detailed behaviour with a settings object on the TestCase (this is a normal hypothesis settings object using the defaults at the time the TestCase class was first referenced). For example if you wanted to run fewer examples with larger programs you could change the settings to: 

 <pre>
TestTrees.settings = settings(max_examples=100, stateful_step_count=100)
</pre> 

 Which doubles the number of steps each program runs and halves the number of runs relative to the example. settings.timeout will also be respected as usual.

<h3>Preconditions</h3>

 

 While it's possible to use <b>assume()</b> in RuleBasedStateMachine rules, if you use it in only a few rules you can quickly run into a situation where few or none of your rules pass their assumptions. Thus, Hypothesis provides a <b>precondition()</b> decorator to avoid this problem. The <b>precondition()</b> decorator is used on <b>rule</b>-decorated functions, and must be given a function that returns True or False based on the RuleBasedStateMachine instance.
<dl>
<dt><b>hypothesis.stateful.precondition(precond)</b>
<dd> Decorator to apply a precondition for rules in a RuleBasedStateMachine. Specifies a precondition for a rule to be considered as a valid step in the state machine. The given function will be called with the instance of RuleBasedStateMachine and should return True or False. Usually it will need to look at attributes on that instance. 

 For example: 

 <pre>
class MyTestMachine(RuleBasedStateMachine):
    state = 1
    @precondition(lambda self: self.state != 0)
    @rule(numerator=integers())
    def divide_with(self, numerator):
        self.state = numerator / self.state
</pre> 

 This is better than using assume in your rule since more valid rules should be able to be run. 

 <pre>
from hypothesis.stateful import RuleBasedStateMachine, rule, precondition
class NumberModifier(RuleBasedStateMachine):
    num = 0
    @rule()
    def add_one(self):
        self.num += 1
    @precondition(lambda self: self.num != 0)
    @rule()
    def divide_with_one(self):
        self.num = 1 / self.num
</pre> 

 By using <b>precondition()</b> here instead of <b>assume()</b>, Hypothesis can filter the inapplicable rules before running them. This makes it much more likely that a useful sequence of steps will be generated. 

 Note that currently preconditions can't access bundles; if you need to use preconditions, you should store relevant data on the instance instead.</dl>

<h3>Invariant</h3>

 

 Often there are invariants that you want to ensure are met after every step in a process. It would be possible to add these as rules that are run, but they would be run zero or multiple times between other rules. Hypothesis provides a decorator that marks a function to be run after every step.
<dl>
<dt><b>hypothesis.stateful.invariant()</b>
<dd> Decorator to apply an invariant for rules in a RuleBasedStateMachine. The decorated function will be run after every rule and can raise an exception to indicate failed invariants. 

 For example: 

 <pre>
class MyTestMachine(RuleBasedStateMachine):
    state = 1
    @invariant()
    def is_nonzero(self):
        assert self.state != 0
</pre> 

 <pre>
from hypothesis.stateful import RuleBasedStateMachine, rule, invariant
class NumberModifier(RuleBasedStateMachine):
    num = 0
    @rule()
    def add_two(self):
        self.num += 2
        if self.num &gt; 50:
            self.num += 1
    @invariant()
    def divide_with_one(self):
        assert self.num % 2 == 0
NumberTest = NumberModifier.TestCase
</pre> 

 Invariants can also have <b>precondition()</b>s applied to them, in which case they will only be run if the precondition function returns true. 

 Note that currently invariants can't access bundles; if you need to use invariants, you should store relevant data on the instance instead.</dl>

<h3>Generic state machines</h3>

 

 The class GenericStateMachine is the underlying machinery of stateful testing in Hypothesis. In execution it looks much like the RuleBasedStateMachine but it allows the set of steps available to depend in essentially arbitrary ways on what has happened so far. For example, if you wanted to use Hypothesis to test a game, it could choose each step in the machine based on the game to date and the set of actions the game program is telling it it has available. 

 It essentially executes the following loop: 

 <pre>
machine = MyStateMachine()
try:
    machine.check_invariants()
    for _ in range(n_steps):
        step = machine.steps().example()
        machine.execute_step(step)
        machine.check_invariants()
finally:
    machine.teardown()
</pre> 

 Where <b>steps</b> and <b>execute_step</b> are methods you must implement, and <b>teardown</b> and <b>check_invarants</b> are methods you can implement if required. <b>steps</b> returns a strategy, which is allowed to depend arbitrarily on the current state of the test execution. <i>Ideally</i> a good steps implementation should be robust against minor changes in the state. Steps that change a lot between slightly different executions will tend to produce worse quality examples because they're hard to simplify. 

 The steps method <i>may</i> depend on external state, but it's not advisable and may produce flaky tests. 

 If any of <b>execute_step</b>, <b>check_invariants</b> or <b>teardown</b> produces an exception, Hypothesis will try to find a minimal sequence of values steps such that the following throws an exception: 

 <pre>
machine = MyStateMachine()
try:
    machine.check_invariants()
    for step in steps:
        machine.execute_step(step)
        machine.check_invariants()
finally:
    machine.teardown()
</pre> 

 and such that at every point, the step executed is one that could plausible have come from a call to <b>steps</b> in the current state. 

 Here's an example of using stateful testing to test a broken implementation of a set in terms of a list (note that you could easily do something close to this example with the rule based testing instead, and probably should. This is mostly for illustration purposes): 

 <pre>
import unittest
from hypothesis.stateful import GenericStateMachine
from hypothesis.strategies import tuples, sampled_from, just, integers
class BrokenSet(GenericStateMachine):
    def __init__(self):
        self.data = []
    def steps(self):
        add_strategy = tuples(just(&quot;add&quot;), integers())
        if not self.data:
            return add_strategy
        else:
            return (
                add_strategy |
                tuples(just(&quot;delete&quot;), sampled_from(self.data)))
    def execute_step(self, step):
        action, value = step
        if action == 'delete':
            try:
                self.data.remove(value)
            except ValueError:
                pass
            assert value not in self.data
        else:
            assert action == 'add'
            self.data.append(value)
            assert value in self.data
TestSet = BrokenSet.TestCase
if __name__ == '__main__':
    unittest.main()
</pre> 

 Note that the strategy changes each time based on the data that's currently in the state machine. 

 Running this gives us the following: 

 <pre>
Step #1: ('add', 0)
Step #2: ('add', 0)
Step #3: ('delete', 0)
F
======================================================================
FAIL: runTest (hypothesis.stateful.BrokenSet.TestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
(...)
    assert value not in self.data
AssertionError
</pre> 

 So it adds two elements, then deletes one, and throws an assertion when it finds out that this only deleted one of the copies of the element.

<h3>More fine grained control</h3>

 

 If you want to bypass the TestCase infrastructure you can invoke these manually. The stateful module exposes the function run_state_machine_as_test, which takes an arbitrary function returning a GenericStateMachine and an optional settings parameter and does the same as the class based runTest provided. 

 In particular this may be useful if you wish to pass parameters to a custom __init__ in your subclass.

<h2>COMPATIBILITY</h2>

 

 Hypothesis does its level best to be compatible with everything you could possibly need it to be compatible with. Generally you should just try it and expect it to work. If it doesn't, you can be surprised and check this document for the details.

<h3>Python versions</h3>

 

 Hypothesis is supported and tested on CPython 2.7 and CPython 3.4+. 

 Hypothesis also supports PyPy2, and will support PyPy3 when there is a stable release supporting Python 3.4+. Hypothesis does not currently work on Jython, though could feasibly be made to do so. IronPython might work but hasn't been tested. 32-bit and narrow builds should work, though this is currently only tested on Windows. 

 In general Hypothesis does not officially support anything except the latest patch release of any version of Python it supports. Earlier releases should work and bugs in them will get fixed if reported, but they're not tested in CI and no guarantees are made.

<h3>Operating systems</h3>

 

 In theory Hypothesis should work anywhere that Python does. In practice it is only known to work and regularly tested on OS X, Windows and Linux, and you may experience issues running it elsewhere. 

 If you're using something else and it doesn't work, do get in touch and I'll try to help, but unless you can come up with a way for me to run a CI server on that operating system it probably won't stay fixed due to the inevitable march of time.

<h3>Testing frameworks</h3>

 

 In general Hypothesis goes to quite a lot of effort to generate things that look like normal Python test functions that behave as closely to the originals as possible, so it should work sensibly out of the box with every test framework. 

 If your testing relies on doing something other than calling a function and seeing if it raises an exception then it probably <i>won't</i> work out of the box. In particular things like tests which return generators and expect you to do something with them (e.g. nose's yield based tests) will not work. Use a decorator or similar to wrap the test to take this form. 

 In terms of what's actually <i>known</i> to work:
<dl>
<dt>&bull;
<dd> Hypothesis integrates as smoothly with py.test and unittest as I can make it, and this is verified as part of the CI.
<dt>&bull;
<dd> py.test fixtures work correctly with Hypothesis based functions, but note that function based fixtures will only run once for the whole function, not once per example.
<dt>&bull;
<dd> Nose works fine with hypothesis, and this is tested as part of the CI. yield based tests simply won't work.
<dt>&bull;
<dd> Integration with Django's testing requires use of the <i>hypothesis-django</i> package. The issue is that in Django's tests' normal mode of execution it will reset the database one per test rather than once per example, which is not what you want. 

 Coverage works out of the box with Hypothesis (and Hypothesis has 100% branch coverage in its own tests). However you should probably not use Coverage, Hypothesis and PyPy together. Because Hypothesis does quite a lot of CPU heavy work compared to normal tests, it really exacerbates the performance problems the two normally have working together.</dl>

<h3>Optional Packages</h3>

 

 The supported versions of optional packages, for strategies in <b>hypothesis.extra</b>, are listed in the documentation for that extra. Our general goal is to support all versions that are supported upstream.

<h3>Regularly verifying this</h3>

 

 Everything mentioned above as explicitly supported is checked on every commit with <i>Travis</i> and <i>Appveyor</i> and goes green before a release happens, so when I say they're supported I really mean it.

<h3>Hypothesis versions</h3>

 

 Backwards compatibility is better than backporting fixes, so we use <i>semantic versioning</i> and only support the most recent version of Hypothesis. See <b>support</b> for more information.

<h2>SOME MORE EXAMPLES</h2>

 

 This is a collection of examples of how to use Hypothesis in interesting ways. It's small for now but will grow over time. 

 All of these examples are designed to be run under <i>py.test</i> (<i>nose</i> should probably work too).

<h3>How not to sort by a partial order</h3>

 

 The following is an example that's been extracted and simplified from a real bug that occurred in an earlier version of Hypothesis. The real bug was a lot harder to find. 

 Suppose we've got the following type: 

 <pre>
class Node(object):
    def __init__(self, label, value):
        self.label = label
        self.value = tuple(value)
    def __repr__(self):
        return &quot;Node(%r, %r)&quot; % (self.label, self.value)
    def sorts_before(self, other):
        if len(self.value) &gt;= len(other.value):
            return False
        return other.value[:len(self.value)] == self.value
</pre> 

 Each node is a label and a sequence of some data, and we have the relationship sorts_before meaning the data of the left is an initial segment of the right. So e.g. a node with value <b>[1, 2]</b> will sort before a node with value <b>[1, 2, 3]</b>, but neither of <b>[1, 2]</b> nor <b>[1, 3]</b> will sort before the other. 

 We have a list of nodes, and we want to topologically sort them with respect to this ordering. That is, we want to arrange the list so that if <b>x.sorts_before(y)</b> then x appears earlier in the list than y. We naively think that the easiest way to do this is to extend the partial order defined here to a total order by breaking ties arbitrarily and then using a normal sorting algorithm. So we define the following code: 

 <pre>
from functools import total_ordering
@total_ordering
class TopoKey(object):
    def __init__(self, node):
        self.value = node
    def __lt__(self, other):
        if self.value.sorts_before(other.value):
            return True
        if other.value.sorts_before(self.value):
            return False
        return self.value.label &lt; other.value.label
def sort_nodes(xs):
    xs.sort(key=TopoKey)
</pre> 

 This takes the order defined by <b>sorts_before</b> and extends it by breaking ties by comparing the node labels. 

 But now we want to test that it works. 

 First we write a function to verify that our desired outcome holds: 

 <pre>
def is_prefix_sorted(xs):
    for i in range(len(xs)):
        for j in range(i+1, len(xs)):
            if xs[j].sorts_before(xs[i]):
                return False
    return True
</pre> 

 This will return false if it ever finds a pair in the wrong order and return true otherwise. 

 Given this function, what we want to do with Hypothesis is assert that for all sequences of nodes, the result of calling <b>sort_nodes</b> on it is sorted. 

 First we need to define a strategy for Node: 

 <pre>
from hypothesis import settings, strategy
import hypothesis.strategies as s
NodeStrategy = s.builds(
  Node,
  s.integers(),
  s.lists(s.booleans(), average_size=5, max_size=10))
</pre> 

 We want to generate <i>short</i> lists of values so that there's a decent chance of one being a prefix of the other (this is also why the choice of bool as the elements). We then define a strategy which builds a node out of an integer and one of those short lists of booleans. 

 We can now write a test: 

 <pre>
from hypothesis import given
@given(s.lists(NodeStrategy))
def test_sorting_nodes_is_prefix_sorted(xs):
    sort_nodes(xs)
    assert is_prefix_sorted(xs)
</pre> 

 this immediately fails with the following example: 

 <pre>
[Node(0, (False, True)), Node(0, (True,)), Node(0, (False,))]
</pre> 

 The reason for this is that because False is not a prefix of (True, True) nor vice versa, sorting things the first two nodes are equal because they have equal labels. This makes the whole order non-transitive and produces basically nonsense results. 

 But this is pretty unsatisfying. It only works because they have the same label. Perhaps we actually wanted our labels to be unique. Lets change the test to do that. 

 <pre>
def deduplicate_nodes_by_label(nodes):
    table = {}
    for node in nodes:
        table[node.label] = node
    return list(table.values())
NodeSet = s.lists(Node).map(deduplicate_nodes_by_label)
</pre> 

 We define a function to deduplicate nodes by labels, and then map that over a strategy for lists of nodes to give us a strategy for lists of nodes with unique labels. We can now rewrite the test to use that: 

 <pre>
@given(NodeSet)
def test_sorting_nodes_is_prefix_sorted(xs):
    sort_nodes(xs)
    assert is_prefix_sorted(xs)
</pre> 

 Hypothesis quickly gives us an example of this <i>still</i> being wrong: 

 <pre>
[Node(0, (False,)), Node(-1, (True,)), Node(-2, (False, False))])
</pre> 

 Now this is a more interesting example. None of the nodes will sort equal. What is happening here is that the first node is strictly less than the last node because (False,) is a prefix of (False, False). This is in turn strictly less than the middle node because neither is a prefix of the other and -2 &lt; -1. The middle node is then less than the first node because -1 &lt; 0. 

 So, convinced that our implementation is broken, we write a better one: 

 <pre>
def sort_nodes(xs):
    for i in hrange(1, len(xs)):
        j = i - 1
        while j &gt;= 0:
            if xs[j].sorts_before(xs[j+1]):
                break
            xs[j], xs[j+1] = xs[j+1], xs[j]
            j -= 1
</pre> 

 This is just insertion sort slightly modified - we swap a node backwards until swapping it further would violate the order constraints. The reason this works is because our order is a partial order already (this wouldn't produce a valid result for a general topological sorting - you need the transitivity). 

 We now run our test again and it passes, telling us that this time we've successfully managed to sort some nodes without getting it completely wrong. Go us.

<h3>Time zone arithmetic</h3>

 

 This is an example of some tests for pytz which check that various timezone conversions behave as you would expect them to. These tests should all pass, and are mostly a demonstration of some useful sorts of thing to test with Hypothesis, and how the hypothesis-datetime extra package works. 

 <pre>
&gt;&gt;&gt; from datetime import timedelta
&gt;&gt;&gt; from hypothesis.extra.pytz import timezones
&gt;&gt;&gt; # The datetimes strategy is naive by default, so tell it to use timezones
&gt;&gt;&gt; aware_datetimes = datetimes(timezones=timezones())
&gt;&gt;&gt; @given(aware_datetimes, timezones(), timezones())
... def test_convert_via_intermediary(dt, tz1, tz2):
...     &quot;&quot;&quot;Test that converting between timezones is not affected
...     by a detour via another timezone.
...     &quot;&quot;&quot;
...     assert dt.astimezone(tz1).astimezone(tz2) == dt.astimezone(tz2)
&gt;&gt;&gt; @given(aware_datetimes, timezones())
... def test_convert_to_and_fro(dt, tz2):
...     &quot;&quot;&quot;If we convert to a new timezone and back to the old one
...     this should leave the result unchanged.
...     &quot;&quot;&quot;
...     tz1 = dt.tzinfo
...     assert dt == dt.astimezone(tz2).astimezone(tz1)
&gt;&gt;&gt; @given(aware_datetimes, timezones())
... def test_adding_an_hour_commutes(dt, tz):
...     &quot;&quot;&quot;When converting between timezones it shouldn't matter
...     if we add an hour here or add an hour there.
...     &quot;&quot;&quot;
...     an_hour = timedelta(hours=1)
...     assert (dt + an_hour).astimezone(tz) == dt.astimezone(tz) + an_hour
&gt;&gt;&gt; @given(aware_datetimes, timezones())
... def test_adding_a_day_commutes(dt, tz):
...     &quot;&quot;&quot;When converting between timezones it shouldn't matter
...     if we add a day here or add a day there.
...     &quot;&quot;&quot;
...     a_day = timedelta(days=1)
...     assert (dt + a_day).astimezone(tz) == dt.astimezone(tz) + a_day
&gt;&gt;&gt; # And we can check that our tests pass
&gt;&gt;&gt; test_convert_via_intermediary()
&gt;&gt;&gt; test_convert_to_and_fro()
&gt;&gt;&gt; test_adding_an_hour_commutes()
&gt;&gt;&gt; test_adding_a_day_commutes()
</pre>

<h3>Condorcet's Paradox</h3>

 

 A classic paradox in voting theory, called Condorcet's paradox, is that majority preferences are not transitive. That is, there is a population and a set of three candidates A, B and C such that the majority of the population prefer A to B, B to C and C to A. 

 Wouldn't it be neat if we could use Hypothesis to provide an example of this? 

 Well as you can probably guess from the presence of this section, we can! This is slightly surprising because it's not really obvious how we would generate an election given the types that Hypothesis knows about. 

 The trick here turns out to be twofold:
<dl>
<dt>1.
<dd> We can generate a type that is <i>much larger</i> than an election, extract an election out of that, and rely on minimization to throw away all the extraneous detail.
<dt>2.
<dd> We can use assume and rely on Hypothesis's adaptive exploration to focus on the examples that turn out to generate interesting elections 

 Without further ado, here is the code: 

 <pre>
from hypothesis import given, assume
from hypothesis.strategies import integers, lists
from collections import Counter
def candidates(votes):
    return {candidate for vote in votes for candidate in vote}
def build_election(votes):
    &quot;&quot;&quot;
    Given a list of lists we extract an election out of this. We do this
    in two phases:
    1. First of all we work out the full set of candidates present in all
       votes and throw away any votes that do not have that whole set.
    2. We then take each vote and make it unique, keeping only the first
       instance of any candidate.
    This gives us a list of total orderings of some set. It will usually
    be a lot smaller than the starting list, but that's OK.
    &quot;&quot;&quot;
    all_candidates = candidates(votes)
    votes = list(filter(lambda v: set(v) == all_candidates, votes))
    if not votes:
        return []
    rebuilt_votes = []
    for vote in votes:
        rv = []
        for v in vote:
            if v not in rv:
                rv.append(v)
        assert len(rv) == len(all_candidates)
        rebuilt_votes.append(rv)
    return rebuilt_votes
@given(lists(lists(integers(min_value=1, max_value=5))))
def test_elections_are_transitive(election):
    election = build_election(election)
    # Small elections are unlikely to be interesting
    assume(len(election) &gt;= 3)
    all_candidates = candidates(election)
    # Elections with fewer than three candidates certainly can't exhibit
    # intransitivity
    assume(len(all_candidates) &gt;= 3)
    # Now we check if the election is transitive
    # First calculate the pairwise counts of how many prefer each candidate
    # to the other
    counts = Counter()
    for vote in election:
        for i in range(len(vote)):
            for j in range(i+1, len(vote)):
                counts[(vote[i], vote[j])] += 1
    # Now look at which pairs of candidates one has a majority over the
    # other and store that.
    graph = {}
    all_candidates = candidates(election)
    for i in all_candidates:
        for j in all_candidates:
            if counts[(i, j)] &gt; counts[(j, i)]:
                graph.setdefault(i, set()).add(j)
    # Now for each triple assert that it is transitive.
    for x in all_candidates:
        for y in graph.get(x, ()):
            for z in graph.get(y, ()):
                assert x not in graph.get(z, ())
</pre> 

 The example Hypothesis gives me on my first run (your mileage may of course vary) is: 

 <pre>
[[3, 1, 4], [4, 3, 1], [1, 4, 3]]
</pre> 

 Which does indeed do the job: The majority (votes 0 and 1) prefer 3 to 1, the majority (votes 0 and 2) prefer 1 to 4 and the majority (votes 1 and 2) prefer 4 to 3. This is in fact basically the canonical example of the voting paradox, modulo variations on the names of candidates.</dl>

<h3>Fuzzing an HTTP API</h3>

 

 Hypothesis's support for testing HTTP services is somewhat nascent. There are plans for some fully featured things around this, but right now they're probably quite far down the line. 

 But you can do a lot yourself without any explicit support! Here's a script I wrote to throw random data against the API for an entirely fictitious service called Waspfinder (this is only lightly obfuscated and you can easily figure out who I'm actually talking about, but I don't want you to run this code and hammer their API without their permission). 

 All this does is use Hypothesis to generate random JSON data matching the format their API asks for and check for 500 errors. More advanced tests which then use the result and go on to do other things are definitely also possible. 

 <pre>
import unittest
from hypothesis import given, assume, settings, strategies as st
from collections import namedtuple
import requests
import os
import random
import time
import math
# These tests will be quite slow because we have to talk to an external
# service. Also we'll put in a sleep between calls so as to not hammer it.
# As a result we reduce the number of test cases and turn off the timeout.
settings.default.max_examples = 100
settings.default.timeout = -1
Goal = namedtuple(&quot;Goal&quot;, (&quot;slug&quot;,))
# We just pass in our API credentials via environment variables.
waspfinder_token = os.getenv('WASPFINDER_TOKEN')
waspfinder_user = os.getenv('WASPFINDER_USER')
assert waspfinder_token is not None
assert waspfinder_user is not None
GoalData = st.fixed_dictionaries({
    'title': st.text(),
    'goal_type': st.sampled_from([
        &quot;hustler&quot;, &quot;biker&quot;, &quot;gainer&quot;, &quot;fatloser&quot;, &quot;inboxer&quot;,
        &quot;drinker&quot;, &quot;custom&quot;]),
    'goaldate': st.one_of(st.none(), st.floats()),
    'goalval': st.one_of(st.none(), st.floats()),
    'rate': st.one_of(st.none(), st.floats()),
    'initval': st.floats(),
    'panic': st.floats(),
    'secret': st.booleans(),
    'datapublic': st.booleans(),
})
needs2 = ['goaldate', 'goalval', 'rate']
class WaspfinderTest(unittest.TestCase):
    @given(GoalData)
    def test_create_goal_dry_run(self, data):
        # We want slug to be unique for each run so that multiple test runs
        # don't interfere with eachother. If for some reason some slugs trigger
        # an error and others don't we'll get a Flaky error, but that's OK.
        slug = hex(random.getrandbits(32))[2:]
        # Use assume to guide us through validation we know about, otherwise
        # we'll spend a lot of time generating boring examples.
        # Title must not be empty
        assume(data[&quot;title&quot;])
        # Exactly two of these values should be not None. The other will be
        # inferred by the API.
        assume(len([1 for k in needs2 if data[k] is not None]) == 2)
        for v in data.values():
            if isinstance(v, float):
                assume(not math.isnan(v))
        data[&quot;slug&quot;] = slug
        # The API nicely supports a dry run option, which means we don't have
        # to worry about the user account being spammed with lots of fake goals
        # Otherwise we would have to make sure we cleaned up after ourselves
        # in this test.
        data[&quot;dryrun&quot;] = True
        data[&quot;auth_token&quot;] = waspfinder_token
        for d, v in data.items():
            if v is None:
                data[d] = &quot;null&quot;
            else:
                data[d] = str(v)
        result = requests.post(
            &quot;<a rel="nofollow" HREF="https://waspfinder.example.com/api/v1/users/">https://waspfinder.example.com/api/v1/users/</a>&quot;
            &quot;%s/goals.json&quot; % (waspfinder_user,), data=data)
        # Lets not hammer the API too badly. This will of course make the
        # tests even slower than they otherwise would have been, but that's
        # life.
        time.sleep(1.0)
        # For the moment all we're testing is that this doesn't generate an
        # internal error. If we didn't use the dry run option we could have
        # then tried doing more with the result, but this is a good start.
        self.assertNotEqual(result.status_code, 500)
if __name__ == '__main__':
    unittest.main()
</pre>

<h2>COMMUNITY</h2>

 

 The Hypothesis community is small for the moment but is full of excellent people who can answer your questions and help you out. Please do join us. 

 The two major places for community discussion are:
<dl>
<dt>&bull;
<dd> <i>The mailing list</i>.
<dt>&bull;
<dd> An IRC channel, #hypothesis on freenode, which is more active than the mailing list. 

 Feel free to use these to ask for help, provide feedback, or discuss anything remotely Hypothesis related at all.</dl>

<h3>Code of conduct</h3>

 

 Hypothesis's community is an inclusive space, and everyone in it is expected to abide by a code of conduct. 

 At the high level the code of conduct goes like this:
<dl>
<dt>1.
<dd> Be kind
<dt>2.
<dd> Be respectful
<dt>3.
<dd> Be helpful 

 While it is impossible to enumerate everything that is unkind, disrespectful or unhelpful, here are some specific things that are definitely against the code of conduct:
<dt>1.
<dd> -isms and -phobias (e.g. racism, sexism, transphobia and homophobia) are unkind, disrespectful <i>and</i> unhelpful. Just don't.
<dt>2.
<dd> All software is broken. This is not a moral failing on the part of the authors. Don't give people a hard time for bad code.
<dt>3.
<dd> It's OK not to know things. Everybody was a beginner once, nobody should be made to feel bad for it.
<dt>4.
<dd> It's OK not to <i>want</i> to know something. If you think someone's question is fundamentally flawed, you should still ask permission before explaining what they should actually be asking.
<dt>5.
<dd> Note that &quot;I was just joking&quot; is not a valid defence.</dl>

<h3>What happens when this goes wrong?</h3>

 

 For minor infractions, I'll just call people on it and ask them to apologise and not do it again. You should feel free to do this too if you're comfortable doing so. 

 Major infractions and repeat offenders will be banned from the community. 

 Also, people who have a track record of bad behaviour outside of the Hypothesis community may be banned even if they obey all these rules if their presence is making people uncomfortable. 

 At the current volume level it's not hard for me to pay attention to the whole community, but if you think I've missed something please feel free to alert me. You can either message me as DRMacIver on freenode or send a me an email at <i>david [at] drmaciver.com</i>.

<h2>THE PURPOSE OF HYPOTHESIS</h2>

 

 What is Hypothesis for? 

 From the perspective of a user, the purpose of Hypothesis is to make it easier for you to write better tests. 

 From my perspective as the author, that is of course also a purpose of Hypothesis, but (if you will permit me to indulge in a touch of megalomania for a moment), the larger purpose of Hypothesis is to drag the world kicking and screaming into a new and terrifying age of high quality software. 

 Software is, as they say, eating the world. Software is also <i>terrible</i>. It's buggy, insecure and generally poorly thought out. This combination is clearly a recipe for disaster. 

 And the state of software testing is even worse. Although it's fairly uncontroversial at this point that you <i>should</i> be testing your code, can you really say with a straight face that most projects you've worked on are adequately tested? 

 A lot of the problem here is that it's too hard to write good tests. Your tests encode exactly the same assumptions and fallacies that you had when you wrote the code, so they miss exactly the same bugs that you missed when you wrote the code. 

 Meanwhile, there are all sorts of tools for making testing better that are basically unused. The original Quickcheck is from <i>1999</i> and the majority of developers have not even heard of it, let alone used it. There are a bunch of half-baked implementations for most languages, but very few of them are worth using. 

 The goal of Hypothesis is to bring advanced testing techniques to the masses, and to provide an implementation that is so high quality that it is easier to use them than it is not to use them. Where I can, I will beg, borrow and steal every good idea I can find that someone has had to make software testing better. Where I can't, I will invent new ones. 

 Quickcheck is the start, but I also plan to integrate ideas from fuzz testing (a planned future feature is to use coverage information to drive example selection, and the example saving database is already inspired by the workflows people use for fuzz testing), and am open to and actively seeking out other suggestions and ideas. 

 The plan is to treat the social problem of people not using these ideas as a bug to which there is a technical solution: Does property-based testing not match your workflow? That's a bug, let's fix it by figuring out how to integrate Hypothesis into it. Too hard to generate custom data for your application? That's a bug. Let's fix it by figuring out how to make it easier, or how to take something you're already using to specify your data and derive a generator from that automatically. Find the explanations of these advanced ideas hopelessly obtuse and hard to follow? That's a bug. Let's provide you with an easy API that lets you test your code better without a PhD in software verification. 

 Grand ambitions, I know, and I expect ultimately the reality will be somewhat less grand, but so far in about three months of development, Hypothesis has become the most solid implementation of Quickcheck ever seen in a mainstream language (as long as we don't count Scala as mainstream yet), and at the same time managed to significantly push forward the state of the art, so I think there's reason to be optimistic.

<h2>TESTIMONIALS</h2>

 

 This is a page for listing people who are using Hypothesis and how excited they are about that. If that's you and your name is not on the list, <i>this file is in Git</i> and I'd love it if you sent me a pull request to fix that.

<h3><i>Stripe</i></h3>

 

 At Stripe we use Hypothesis to test every piece of our machine learning model training pipeline (powered by scikit). Before we migrated, our tests were filled with hand-crafted pandas Dataframes that weren't representative at all of our actual very complex data. Because we needed to craft examples for each test, we took the easy way out and lived with extremely low test coverage. 

 Hypothesis changed all that. Once we had our strategies for generating Dataframes of features it became trivial to slightly customize each strategy for new tests. Our coverage is now close to 90%. 

 Full-stop, property-based testing is profoundly more powerful - and has caught or prevented far more bugs - than our old style of example-based testing.

<h3>Kristian Glass - Director of Technology at <i>LaterPay GmbH</i></h3>

 

 Hypothesis has been brilliant for expanding the coverage of our test cases, and also for making them much easier to read and understand, so we're sure we're testing the things we want in the way we want.

<h3><i>Seth Morton</i></h3>

 

 When I first heard about Hypothesis, I knew I had to include it in my two open-source Python libraries, <i>natsort</i> and <i>fastnumbers</i> . Quite frankly, I was a little appalled at the number of bugs and &quot;holes&quot; I found in the code. I can now say with confidence that my libraries are more robust to &quot;the wild.&quot; In addition, Hypothesis gave me the confidence to expand these libraries to fully support Unicode input, which I never would have had the stomach for without such thorough testing capabilities. Thanks!

<h3><i>Sixty North</i></h3>

 

 At Sixty North we use Hypothesis for testing <i>Segpy</i> an open source Python library for shifting data between Python data structures and SEG Y files which contain geophysical data from the seismic reflection surveys used in oil and gas exploration. 

 This is our first experience of property-based testing â as opposed to example-based testing. Not only are our tests more powerful, they are also much better explanations of what we expect of the production code. In fact, the tests are much closer to being specifications. Hypothesis has located real defects in our code which went undetected by traditional test cases, simply because Hypothesis is more relentlessly devious about test case generation than us mere humans! We found Hypothesis particularly beneficial for Segpy because SEG Y is an antiquated format that uses legacy text encodings (EBCDIC) and even a legacy floating point format we implemented from scratch in Python. 

 Hypothesis is sure to find a place in most of our future Python codebases and many existing ones too.

<h3><i>mulkieran</i></h3>

 

 Just found out about this excellent QuickCheck for Python implementation and ran up a few tests for my <i>bytesize</i> package last night. Refuted a few hypotheses in the process. 

 Looking forward to using it with a bunch of other projects as well.

<h3><i>Adam Johnson</i></h3>

 

 I have written a small library to serialize <b>dict</b>s to MariaDB's dynamic columns binary format, <i>mariadb-dyncol</i>. When I first developed it, I thought I had tested it really well - there were hundreds of test cases, some of them even taken from MariaDB's test suite itself. I was ready to release. 

 Lucky for me, I tried Hypothesis with David at the PyCon UK sprints. Wow! It found bug after bug after bug. Even after a first release, I thought of a way to make the tests do more validation, which revealed a further round of bugs! Most impressively, Hypothesis found a complicated off-by-one error in a condition with 4095 versus 4096 bytes of data - something that I would never have found. 

 Long live Hypothesis! (Or at least, property-based testing).

<h3><i>Josh Bronson</i></h3>

 

 Adopting Hypothesis improved <i>bidict</i>'s test coverage and significantly increased our ability to make changes to the code with confidence that correct behavior would be preserved. Thank you, David, for the great testing tool.

<h3><i>Cory Benfield</i></h3>

 

 Hypothesis is the single most powerful tool in my toolbox for working with algorithmic code, or any software that produces predictable output from a wide range of sources. When using it with <i>Priority</i>, Hypothesis consistently found errors in my assumptions and extremely subtle bugs that would have taken months of real-world use to locate. In some cases, Hypothesis found subtle deviations from the correct output of the algorithm that may never have been noticed at all. 

 When it comes to validating the correctness of your tools, nothing comes close to the thoroughness and power of Hypothesis.

<h3><i>Jon Moore</i></h3>

 

 One extremely satisfied user here. Hypothesis is a really solid implementation of property-based testing, adapted well to Python, and with good features such as failure-case shrinkers. I first used it on a project where we needed to verify that a vendor's Python and non-Python implementations of an algorithm matched, and it found about a dozen cases that previous example-based testing and code inspections had not. Since then I've been evangelizing for it at our firm.

<h3><i>Russel Winder</i></h3>

 

 I am using Hypothesis as an integral part of my Python workshops. Testing is an integral part of Python programming and whilst unittest and, better, py.test can handle example-based testing, property-based testing is increasingly far more important than example-base testing, and Hypothesis fits the bill.

<h3><i>Wellfire Interactive</i></h3>

 

 We've been using Hypothesis in a variety of client projects, from testing Django-related functionality to domain-specific calculations. It both speeds up and simplifies the testing process since there's so much less tedious and error-prone work to do in identifying edge cases. Test coverage is nice but test depth is even nicer, and it's much easier to get meaningful test depth using Hypothesis.

<h3><i>Your name goes here</i></h3>

 

 I know there are many more, because I keep finding out about new people I'd never even heard of using Hypothesis. If you're looking to way to give back to a tool you love, adding your name here only takes a moment and would really help a lot. As per instructions at the top, just send me a pull request and I'll add you to the list.

<h2>OPEN SOURCE PROJECTS USING HYPOTHESIS</h2>

 

 The following is a non-exhaustive list of open source projects I know are using Hypothesis. If you're aware of any others please add them to the list! The only inclusion criterion right now is that if it's a Python library then it should be available on pypi.
<dl>
<dt>&bull;
<dd> <i>aur</i>
<dt>&bull;
<dd> <i>axelrod</i>
<dt>&bull;
<dd> <i>bidict</i>
<dt>&bull;
<dd> <i>binaryornot</i>
<dt>&bull;
<dd> <i>brotlipy</i>
<dt>&bull;
<dd> <i>chardet</i>
<dt>&bull;
<dd> <i>cmph-cffi</i>
<dt>&bull;
<dd> <i>cryptography</i>
<dt>&bull;
<dd> <i>dbus-signature-pyparsing</i>
<dt>&bull;
<dd> <i>fastnumbers</i>
<dt>&bull;
<dd> <i>flocker</i>
<dt>&bull;
<dd> <i>flownetpy</i>
<dt>&bull;
<dd> <i>funsize</i>
<dt>&bull;
<dd> <i>fusion-index</i>
<dt>&bull;
<dd> <i>hyper-h2</i>
<dt>&bull;
<dd> <i>into-dbus-python</i>
<dt>&bull;
<dd> <i>justbases</i>
<dt>&bull;
<dd> <i>justbytes</i>
<dt>&bull;
<dd> <i>mariadb-dyncol</i>
<dt>&bull;
<dd> <i>mercurial</i>
<dt>&bull;
<dd> <i>natsort</i>
<dt>&bull;
<dd> <i>pretext</i>
<dt>&bull;
<dd> <i>priority</i>
<dt>&bull;
<dd> <i>PyCEbox</i>
<dt>&bull;
<dd> <i>PyPy</i>
<dt>&bull;
<dd> <i>pyrsistent</i>
<dt>&bull;
<dd> <i>pyudev</i>
<dt>&bull;
<dd> <i>qutebrowser</i>
<dt>&bull;
<dd> <i>RubyMarshal</i>
<dt>&bull;
<dd> <i>Segpy</i>
<dt>&bull;
<dd> <i>simoa</i>
<dt>&bull;
<dd> <i>srt</i>
<dt>&bull;
<dd> <i>tchannel</i>
<dt>&bull;
<dd> <i>vdirsyncer</i>
<dt>&bull;
<dd> <i>wcag-contrast-ratio</i>
<dt>&bull;
<dd> <i>yacluster</i>
<dt>&bull;
<dd> <i>yturl</i></dl>

<h2>PROJECTS EXTENDING HYPOTHESIS</h2>

 

 The following is a non-exhaustive list of open source projects that make Hypothesis strategies available. If you're aware of any others please add them the list! The only inclusion criterion right now is that if it's a Python library then it should be available on pypi.
<dl>
<dt>&bull;
<dd> <i>hs-dbus-signature</i> - strategy to generate arbitrary D-Bus signatures
<dt>&bull;
<dd> <i>hypothesis-regex</i> - strategy to generate strings that match given regular expression.
<dt>&bull;
<dd> <i>lollipop-hypothesis</i> - strategy to generate data based on <i>Lollipop</i> schema definitions. 

 If you're thinking about writing an extension, consider naming it <b>hypothesis-{something}</b> - a standard prefix makes the community more visible and searching for extensions easier.</dl>

<h2>CHANGELOG</h2>

 

 This is a record of all past Hypothesis releases and what went into them, in reverse chronological order. All previous releases should still be available on pip. 

 Hypothesis APIs come in three flavours:
<dl>
<dt>&bull;
<dd> Public: Hypothesis releases since 1.0 are <i>semantically versioned</i> with respect to these parts of the API. These will not break except between major version bumps. All APIs mentioned in this documentation are public unless explicitly noted otherwise.
<dt>&bull;
<dd> Semi-public: These are APIs that are considered ready to use but are not wholly nailed down yet. They will not break in patch releases and will <i>usually</i> not break in minor releases, but when necessary minor releases may break semi-public APIs.
<dt>&bull;
<dd> Internal: These may break at any time and you really should not use them at all. 

 You should generally assume that an API is internal unless you have specific information to the contrary.</dl>

<h3>3.12.0 - 2017-07-07</h3>

 

 This release makes some major internal changes to how Hypothesis represents data internally, as a prelude to some major engine changes that should improve data quality. There are no API changes, but it's a significant enough internal change that a minor version bump seemed warranted. 

 User facing impact should be fairly mild, but includes:
<dl>
<dt>&bull;
<dd> All existing examples in the database will probably be invalidated. Hypothesis handles this automatically, so you don't need to do anything, but if you see all your examples disappear that's why.
<dt>&bull;
<dd> Almost all data distributions have changed significantly. Possibly for the better, possibly for the worse. This may result in new bugs being found, but it may also result in Hypothesis being unable to find bugs it previously did.
<dt>&bull;
<dd> Data generation may be somewhat faster if your existing bottleneck was in draw_bytes (which is often the case for large examples).
<dt>&bull;
<dd> Shrinking will probably be slower, possibly significantly. 

 If you notice any effects you consider to be a significant regression, please open an issue about them.</dl>

<h3>3.11.6 - 2017-06-19</h3>

 

 This release involves no functionality changes, but is the first to ship wheels as well as an sdist.

<h3>3.11.5 - 2017-06-18</h3>

 

 This release provides a performance improvement to shrinking. For cases where there is some non-trivial &quot;boundary&quot; value (e.g. the bug happens for all values greater than some other value), shrinking should now be substantially faster. Other types of bug will likely see improvements too. 

 This may also result in some changes to the quality of the final examples - it may sometimes be better, but is more likely to get slightly worse in some edge cases. If you see any examples where this happens in practice, please report them.

<h3>3.11.4 - 2017-06-17</h3>

 

 This is a bugfix release: Hypothesis now prints explicit examples when running in verbose mode. (<i>issue #313</i>)

<h3>3.11.3 - 2017-06-11</h3>

 

 This is a bugfix release: Hypothesis no longer emits a warning if you try to use <b>sampled_from()</b> with <b>python:collections.OrderedDict</b>. (<i>issue #688</i>)

<h3>3.11.2 - 2017-06-10</h3>

 

 This is a documentation release. Several outdated snippets have been updated or removed, and many cross-references are now hyperlinks.

<h3>3.11.1 - 2017-05-28</h3>

 

 This is a minor ergonomics release. Tracebacks shown by pytest no longer include Hypothesis internals for test functions decorated with <b>@given</b>.

<h3>3.11.0 - 2017-05-23</h3>

 

 This is a feature release, adding datetime-related strategies to the core strategies. 

 <b>timezones()</b> allows you to sample pytz timezones from the Olsen database. Use directly in a recipe for tz-aware datetimes, or compose with <b>none()</b> to allow a mix of aware and naive output. 

 The new <b>dates()</b>, <b>times()</b>, <b>datetimes()</b>, and <b>timedeltas()</b> strategies are all constrained by objects of their type. This means that you can generate dates bounded by a single day (i.e. a single date), or datetimes constrained to the microsecond. 

 <b>times()</b> and <b>datetimes()</b> take an optional <b>timezones=</b> argument, which defaults to <b>none()</b> for naive times. You can use our extra strategy based on pytz, or roll your own timezones strategy with dateutil or even the standard library. 

 The old <b>dates</b>, <b>times</b>, and <b>datetimes</b> strategies in <b>hypothesis.extra.datetimes</b> are deprecated in favor of the new core strategies, which are more flexible and have no dependencies.

<h3>3.10.0 - 2017-05-22</h3>

 

 Hypothesis now uses <b>python:inspect.getfullargspec()</b> internally. On Python 2, there are no visible changes. 

 On Python 3 <b>@given</b> and <b>@composite</b> now preserve <i>PEP 3107</i> annotations on the decorated function. Keyword-only arguments are now either handled correctly (e.g. <b>@composite</b>), or caught in validation instead of silently discarded or raising an unrelated error later (e.g. <b>@given</b>).

<h3>3.9.1 - 2017-05-22</h3>

 

 This is a bugfix release: the default field mapping for a DateTimeField in the Django extra now respects the <b>USE_TZ</b> setting when choosing a strategy.

<h3>3.9.0 - 2017-05-19</h3>

 

 This is feature release, expanding the capabilities of the <b>decimals()</b> strategy.
<dl>
<dt>&bull;
<dd> The new (optional) <b>places</b> argument allows you to generate decimals with a certain number of places (e.g. cents, thousandths, satoshis).
<dt>&bull;
<dd> If allow_infinity is None, setting min_bound no longer excludes positive infinity and setting max_value no longer excludes negative infinity.
<dt>&bull;
<dd> All of <b>NaN</b>, <b>-Nan</b>, <b>sNaN</b>, and <b>-sNaN</b> may now be drawn if allow_nan is True, or if allow_nan is None and min_value or max_value is None.
<dt>&bull;
<dd> min_value and max_value may be given as decimal strings, e.g. <b>&quot;1.234&quot;</b>.</dl>

<h3>3.8.5 - 2017-05-16</h3>

 

 Hypothesis now imports <b>python:sqlite3</b> when a SQLite database is used, rather than at module load, improving compatibility with Python implementations compiled without SQLite support (such as BSD or Jython).

<h3>3.8.4 - 2017-05-16</h3>

 

 This is a compatibility bugfix release. <b>sampled_from</b> no longer raises a deprecation warning when sampling from an <b>Enum</b>, as all enums have a reliable iteration order.

<h3>3.8.3 - 2017-05-09</h3>

 

 This release removes a version check for older versions of pytest when using the Hypothesis pytest plugin. The pytest plugin will now run unconditionally on all versions of pytest. This breaks compatibility with any version of pytest prior to 2.7.0 (which is more than two years old). 

 The primary reason for this change is that the version check was a frequent source of breakage when pytest change their versioning scheme. If you are not working on pytest itself and are not running a very old version of it, this release probably doesn't affect you.

<h3>3.8.2 - 2017-04-26</h3>

 

 This is a code reorganisation release that moves some internal test helpers out of the main source tree so as to not have changes to them trigger releases in future.

<h3>3.8.1 - 2017-04-26</h3>

 

 This is a documentation release. Almost all code examples are now doctests checked in CI, eliminating stale examples.

<h3>3.8.0 - 2017-04-23</h3>

 

 This is a feature release, adding the <b>iterables()</b> strategy, equivalent to <b>lists(...).map(iter)</b> but with a much more useful repr. You can use this strategy to check that code doesn't accidentally depend on sequence properties such as indexing support or repeated iteration.

<h3>3.7.4 - 2017-04-22</h3>

 

 This is a bug fix release for a single bug:
<dl>
<dt>&bull;
<dd> In 3.7.3, using <b>@example</b> and a pytest fixture in the same test could cause the test to fail to fill the arguments, and throw a TypeError.</dl>

<h3>3.7.3 - 2017-04-21</h3>

 

 This release should include no user visible changes and is purely a refactoring release. This modularises the behaviour of the core <b>given()</b> function, breaking it up into smaller and more accessible parts, but its actual behaviour should remain unchanged.

<h3>3.7.2 - 2017-04-21</h3>

 

 This reverts an undocumented change in 3.7.1 which broke installation on debian stable: The specifier for the hypothesis[django] extra_requires had introduced a wild card, which was not supported on the default version of pip.

<h3>3.7.1 - 2017-04-21</h3>

 

 This is a bug fix and internal improvements release.
<dl>
<dt>&bull;
<dd> In particular Hypothesis now tracks a tree of where it has already explored. This allows it to avoid some classes of duplicate examples, and significantly improves the performance of shrinking failing examples by allowing it to skip some shrinks that it can determine can't possibly work.
<dt>&bull;
<dd> Hypothesis will no longer seed the global random arbitrarily unless you have asked it to using <b>random_module()</b>
<dt>&bull;
<dd> Shrinking would previously have not worked correctly in some special cases on Python 2, and would have resulted in suboptimal examples.</dl>

<h3>3.7.0 - 2017-03-20</h3>

 

 This is a feature release. 

 New features:
<dl>
<dt>&bull;
<dd> Rule based stateful testing now has an <b>@invariant</b> decorator that specifies methods that are run after init and after every step, allowing you to encode properties that should be true at all times. Thanks to Tom Prince for this feature.
<dt>&bull;
<dd> The <b>decimals()</b> strategy now supports <b>allow_nan</b> and <b>allow_infinity</b> flags.
<dt>&bull;
<dd> There are <i>significantly more strategies available for numpy</i>, including for generating arbitrary data types. Thanks to Zac Hatfield Dodds for this feature.
<dt>&bull;
<dd> When using the <b>data()</b> strategy you can now add a label as an argument to <b>draw()</b>, which will be printed along with the value when an example fails. Thanks to Peter Inglesby for this feature. 

 Bug fixes:
<dt>&bull;
<dd> Bug fix: <b>composite()</b> now preserves functions' docstrings.
<dt>&bull;
<dd> The build is now reproducible and doesn't depend on the path you build it from. Thanks to Chris Lamb for this feature.
<dt>&bull;
<dd> numpy strategies for the void data type did not work correctly. Thanks to Zac Hatfield Dodds for this fix. 

 There have also been a number of performance optimizations:
<dt>&bull;
<dd> The <b>permutations()</b> strategy is now significantly faster to use for large lists (the underlying algorithm has gone from O(n^2) to <a HREF="/docs/linux/man/n-o/">O</a>(n)).
<dt>&bull;
<dd> Shrinking of failing test cases should have got significantly faster in some circumstances where it was previously struggling for a long time.
<dt>&bull;
<dd> Example generation now involves less indirection, which results in a small speedup in some cases (small enough that you won't really notice it except in pathological cases).</dl>

<h3>3.6.1 - 2016-12-20</h3>

 

 This release fixes a dependency problem and makes some small behind the scenes improvements.
<dl>
<dt>&bull;
<dd> The fake-factory dependency was renamed to faker. If you were depending on it through hypothesis[django] or hypothesis[fake-factory] without pinning it yourself then it would have failed to install properly. This release changes it so that hypothesis[fakefactory] (which can now also be installed as hypothesis[faker]) will install the renamed faker package instead.
<dt>&bull;
<dd> This release also removed the dependency of hypothesis[django] on hypothesis[fakefactory] - it was only being used for emails. These now use a custom strategy that isn't from fakefactory. As a result you should also see performance improvements of tests which generated User objects or other things with email fields, as well as better shrinking of email addresses.
<dt>&bull;
<dd> The distribution of code using nested calls to <b>one_of()</b> or the <b>|</b> operator for combining strategies has been improved, as branches are now flattened to give a more uniform distribution.
<dt>&bull;
<dd> Examples using <b>composite()</b> or <b>.flatmap</b> should now shrink better. In particular this will affect things which work by first generating a length and then generating that many items, which have historically not shrunk very well.</dl>

<h3>3.6.0 - 2016-10-31</h3>

 

 This release reverts Hypothesis to its old pretty printing of lambda functions based on attempting to extract the source code rather than decompile the bytecode. This is unfortunately slightly inferior in some cases and may result in you occasionally seeing things like <b>lambda x: &lt;unknown&gt;</b> in statistics reports and strategy reprs. 

 This removes the dependencies on uncompyle6, xdis and spark-parser. 

 The reason for this is that the new functionality was based on uncompyle6, which turns out to introduce a hidden GPLed dependency - it in turn depended on xdis, and although the library was licensed under the MIT license, it contained some GPL licensed source code and thus should have been released under the GPL. 

 My interpretation is that Hypothesis itself was never in violation of the GPL (because the license it is under, the Mozilla Public License v2, is fully compatible with being included in a GPL licensed work), but I have not consulted a lawyer on the subject. Regardless of the answer to this question, adding a GPLed dependency will likely cause a lot of users of Hypothesis to inadvertently be in violation of the GPL. 

 As a result, if you are running Hypothesis 3.5.x you really should upgrade to this release immediately.

<h3>3.5.3 - 2016-10-05</h3>

 

 This is a bug fix release. 

 Bugs fixed:
<dl>
<dt>&bull;
<dd> If the same test was running concurrently in two processes and there were examples already in the test database which no longer failed, Hypothesis would sometimes fail with a FileNotFoundError (IOError on Python 2) because an example it was trying to read was deleted before it was read. (<i>issue #372</i>).
<dt>&bull;
<dd> Drawing from an <b>integers()</b> strategy with both a min_value and a max_value would reject too many examples needlessly. Now it repeatedly redraws until satisfied. (<i>pull request #366</i>. Thanks to Calen Pennington for the contribution).</dl>

<h3>3.5.2 - 2016-09-24</h3>

 

 This is a bug fix release.
<dl>
<dt>&bull;
<dd> The Hypothesis pytest plugin broke pytest support for doctests. Now it doesn't.</dl>

<h3>3.5.1 - 2016-09-23</h3>

 

 This is a bug fix release.
<dl>
<dt>&bull;
<dd> Hypothesis now runs cleanly in -B and -BB modes, avoiding mixing bytes and unicode.
<dt>&bull;
<dd> <b>python:unittest.TestCase</b> tests would not have shown up in the new statistics mode. Now they do.
<dt>&bull;
<dd> Similarly, stateful tests would not have shown up in statistics and now they do.
<dt>&bull;
<dd> Statistics now print with pytest node IDs (the names you'd get in pytest verbose mode).</dl>

<h3>3.5.0 - 2016-09-22</h3>

 

 This is a feature release.
<dl>
<dt>&bull;
<dd> <b>fractions()</b> and <b>decimals()</b> strategies now support min_value and max_value parameters. Thanks go to Anne Mulhern for the development of this feature.
<dt>&bull;
<dd> The Hypothesis pytest plugin now supports a --hypothesis-show-statistics parameter that gives detailed statistics about the tests that were run. Huge thanks to Jean-Louis Fuchs and Adfinis-SyGroup for funding the development of this feature.
<dt>&bull;
<dd> There is a new <b>event()</b> function that can be used to add custom statistics. 

 Additionally there have been some minor bug fixes:
<dt>&bull;
<dd> In some cases Hypothesis should produce fewer duplicate examples (this will mostly only affect cases with a single parameter).
<dt>&bull;
<dd> py.test command line parameters are now under an option group for Hypothesis (thanks to David Keijser for fixing this)
<dt>&bull;
<dd> Hypothesis would previously error if you used <i>PEP 3107</i> function annotations on your tests under Python 3.4.
<dt>&bull;
<dd> The repr of many strategies using lambdas has been improved to include the lambda body (this was previously supported in many but not all cases).</dl>

<h3>3.4.2 - 2016-07-13</h3>

 

 This is a bug fix release, fixing a number of problems with the settings system:
<dl>
<dt>&bull;
<dd> Test functions defined using <b>@given</b> can now be called from other threads (<i>issue #337</i>)
<dt>&bull;
<dd> Attempting to delete a settings property would previously have silently done the wrong thing. Now it raises an AttributeError.
<dt>&bull;
<dd> Creating a settings object with a custom database_file parameter was silently getting ignored and the default was being used instead. Now it's not.</dl>

<h3>3.4.1 - 2016-07-07</h3>

 

 This is a bug fix release for a single bug:
<dl>
<dt>&bull;
<dd> On Windows when running two Hypothesis processes in parallel (e.g. using pytest-xdist) they could race with each other and one would raise an exception due to the non-atomic nature of file renaming on Windows and the fact that you can't rename over an existing file. This is now fixed.</dl>

<h3>3.4.0 - 2016-05-27</h3>

 

 This release is entirely provided by <i>Lucas Wiman</i>: 

 Strategies constructed by <b>models()</b> will now respect much more of Django's validations out of the box. Wherever possible full_clean() should succeed. 

 In particular:
<dl>
<dt>&bull;
<dd> The max_length, blank and choices kwargs are now respected.
<dt>&bull;
<dd> Add support for DecimalField.
<dt>&bull;
<dd> If a field includes validators, the list of validators are used to filter the field strategy.</dl>

<h3>3.3.0 - 2016-05-27</h3>

 

 This release went wrong and is functionally equivalent to 3.2.0. Ignore it.

<h3>3.2.0 - 2016-05-19</h3>

 

 This is a small single-feature release:
<dl>
<dt>&bull;
<dd> All tests using <b>@given</b> now fix the global random seed. This removes the health check for that. If a non-zero seed is required for the final falsifying example, it will be reported. Otherwise Hypothesis will assume randomization was not a significant factor for the test and be silent on the subject. If you use <b>random_module()</b> this will continue to work and will always display the seed.</dl>

<h3>3.1.3 - 2016-05-01</h3>

 

 Single bug fix release
<dl>
<dt>&bull;
<dd> Another charmap problem. In 3.1.2 <b>text()</b> and <b>characters()</b> would break on systems which had <b>/tmp</b> mounted on a different partition than the Hypothesis storage directory (usually in home). This fixes that.</dl>

<h3>3.1.2 - 2016-04-30</h3>

 

 Single bug fix release:
<dl>
<dt>&bull;
<dd> Anything which used a <b>text()</b> or <b>characters()</b> strategy was broken on Windows and I hadn't updated appveyor to use the new repository location so I didn't notice. This is now fixed and windows support should work correctly.</dl>

<h3>3.1.1 - 2016-04-29</h3>

 

 Minor bug fix release.
<dl>
<dt>&bull;
<dd> Fix concurrency issue when running tests that use <b>text()</b> from multiple processes at once (<i>issue #302</i>, thanks to Alex Chan).
<dt>&bull;
<dd> Improve performance of code using <b>lists()</b> with max_size (thanks to Cristi Cobzarenco).
<dt>&bull;
<dd> Fix install on Python 2 with ancient versions of pip so that it installs the enum34 backport (thanks to Donald Stufft for telling me how to do this).
<dt>&bull;
<dd> Remove duplicated __all__ exports from hypothesis.strategies (thanks to PiÃ«t Delport).
<dt>&bull;
<dd> Update headers to point to new repository location.
<dt>&bull;
<dd> Allow use of strategies that can't be used in <b>find()</b> (e.g. <b>choices()</b>) in stateful testing.</dl>

<h3>3.1.0 - 2016-03-06</h3>

<dl>
<dt>&bull;
<dd> Add a <b>nothing()</b> strategy that never successfully generates values.
<dt>&bull;
<dd> <b>sampled_from()</b> and <b>one_of()</b> can both now be called with an empty argument list, in which case they also never generate any values.
<dt>&bull;
<dd> <b>one_of()</b> may now be called with a single argument that is a collection of strategies as well as as varargs.
<dt>&bull;
<dd> Add a <b>runner()</b> strategy which returns the instance of the current test object if there is one.
<dt>&bull;
<dd> 'Bundle' for RuleBasedStateMachine is now a normal(ish) strategy and can be used as such.
<dt>&bull;
<dd> Tests using RuleBasedStateMachine should now shrink significantly better.
<dt>&bull;
<dd> Hypothesis now uses a pretty-printing library internally, compatible with IPython's pretty printing protocol (actually using the same code). This may improve the quality of output in some cases.
<dt>&bull;
<dd> As a 'phases' setting that allows more fine grained control over which parts of the process Hypothesis runs
<dt>&bull;
<dd> Add a suppress_health_check setting which allows you to turn off specific health checks in a fine grained manner.
<dt>&bull;
<dd> Fix a bug where lists of non fixed size would always draw one more element than they included. This mostly didn't matter, but if would cause problems with empty strategies or ones with side effects.
<dt>&bull;
<dd> Add a mechanism to the Django model generator to allow you to explicitly request the default value (thanks to Jeremy Thurgood for this one).</dl>

<h3>3.0.5 - 2016-02-25</h3>

<dl>
<dt>&bull;
<dd> Fix a bug where Hypothesis would now error on py.test development versions.</dl>

<h3>3.0.4 - 2016-02-24</h3>

<dl>
<dt>&bull;
<dd> Fix a bug where Hypothesis would error when running on Python 2.7.3 or earlier because it was trying to pass a <b>python:bytearray</b> object to <b>python:struct.unpack()</b> (which is only supported since 2.7.4).</dl>

<h3>3.0.3 - 2016-02-23</h3>

<dl>
<dt>&bull;
<dd> Fix version parsing of py.test to work with py.test release candidates
<dt>&bull;
<dd> More general handling of the health check problem where things could fail because of a cache miss - now one &quot;free&quot; example is generated before the start of the health check run.</dl>

<h3>3.0.2 - 2016-02-18</h3>

<dl>
<dt>&bull;
<dd> Under certain circumstances, strategies involving <b>text()</b> buried inside some other strategy (e.g. <b>text().filter(...)</b> or <b>recursive(text(), ...))</b> would cause a test to fail its health checks the first time it ran. This was caused by having to compute some related data and cache it to disk. On travis or anywhere else where the <b>.hypothesis</b> directory was recreated this would have caused the tests to fail their health check on every run. This is now fixed for all the known cases, although there could be others lurking.</dl>

<h3>3.0.1 - 2016-02-18</h3>

<dl>
<dt>&bull;
<dd> Fix a case where it was possible to trigger an &quot;Unreachable&quot; assertion when running certain flaky stateful tests.
<dt>&bull;
<dd> Improve shrinking of large stateful tests by eliminating a case where it was hard to delete early steps.
<dt>&bull;
<dd> Improve efficiency of drawing <b>binary(min_size=n, max_size=n)</b> significantly by provide a custom implementation for fixed size blocks that can bypass a lot of machinery.
<dt>&bull;
<dd> Set default home directory based on the current working directory at the point Hypothesis is imported, not whenever the function first happens to be called.</dl>

<h3>3.0.0 - 2016-02-17</h3>

 

 Codename: This really should have been 2.1. 

 Externally this looks like a very small release. It has one small breaking change that probably doesn't affect anyone at all (some behaviour that never really worked correctly is now outright forbidden) but necessitated a major version bump and one visible new feature. 

 Internally this is a complete rewrite. Almost nothing other than the public API is the same. 

 New features:
<dl>
<dt>&bull;
<dd> Addition of <b>data()</b> strategy which allows you to draw arbitrary data interactively within the test.
<dt>&bull;
<dd> New &quot;exploded&quot; database format which allows you to more easily check the example database into a source repository while supporting merging.
<dt>&bull;
<dd> Better management of how examples are saved in the database.
<dt>&bull;
<dd> Health checks will now raise as errors when they fail. It was too easy to have the warnings be swallowed entirely. 

 New limitations:
<dt>&bull;
<dd> <b>choices()</b> and <b>streaming()</b> strategies may no longer be used with <b>find()</b>. Neither may <b>data()</b> (this is the change that necessitated a major version bump). 

 Feature removal:
<dt>&bull;
<dd> The ForkingTestCase executor has gone away. It may return in some more working form at a later date. 

 Performance improvements:
<dt>&bull;
<dd> A new model which allows flatmap, composite strategies and stateful testing to perform <i>much</i> better. They should also be more reliable.
<dt>&bull;
<dd> Filtering may in some circumstances have improved significantly. This will help especially in cases where you have lots of values with individual filters on them, such as lists(x.filter(...)).
<dt>&bull;
<dd> Modest performance improvements to the general test runner by avoiding expensive operations 

 In general your tests should have got faster. If they've instead got significantly slower, I'm interested in hearing about it. 

 Data distribution: 

 The data distribution should have changed significantly. This may uncover bugs the previous version missed. It may also miss bugs the previous version could have uncovered. Hypothesis is now producing less strongly correlated data than it used to, but the correlations are extended over more of the structure. 

 Shrinking: 

 Shrinking quality should have improved. In particular Hypothesis can now perform simultaneous shrinking of separate examples within a single test (previously it was only able to do this for elements of a single collection). In some cases performance will have improved, in some cases it will have got worse but generally shouldn't have by much.</dl>

<h3>2.0.0 - 2016-01-10</h3>

 

 Codename: A new beginning 

 This release cleans up all of the legacy that accrued in the course of Hypothesis 1.0. These are mostly things that were emitting deprecation warnings in 1.19.0, but there were a few additional changes. 

 In particular:
<dl>
<dt>&bull;
<dd> non-strategy values will no longer be converted to strategies when used in given or find.
<dt>&bull;
<dd> FailedHealthCheck is now an error and not a warning.
<dt>&bull;
<dd> Handling of non-ascii reprs in user types have been simplified by using raw strings in more places in Python 2.
<dt>&bull;
<dd> given no longer allows mixing positional and keyword arguments.
<dt>&bull;
<dd> given no longer works with functions with defaults.
<dt>&bull;
<dd> given no longer turns provided arguments into defaults - they will not appear in the argspec at all.
<dt>&bull;
<dd> the basic() strategy no longer exists.
<dt>&bull;
<dd> the n_ary_tree strategy no longer exists.
<dt>&bull;
<dd> the average_list_length setting no longer exists. Note: If you're using using recursive() this will cause you a significant slow down. You should pass explicit average_size parameters to collections in recursive calls.
<dt>&bull;
<dd> @rule can no longer be applied to the same method twice.
<dt>&bull;
<dd> Python 2.6 and 3.3 are no longer officially supported, although in practice they still work fine. 

 This also includes two non-deprecation changes:
<dt>&bull;
<dd> given's keyword arguments no longer have to be the rightmost arguments and can appear anywhere in the method signature.
<dt>&bull;
<dd> The max_shrinks setting would sometimes not have been respected.</dl>

<h3>1.19.0 - 2016-01-09</h3>

 

 Codename: IT COMES 

 This release heralds the beginning of a new and terrible age of Hypothesis 2.0. 

 It's primary purpose is some final deprecations prior to said release. The goal is that if your code emits no warnings under this release then it will probably run unchanged under Hypothesis 2.0 (there are some caveats to this: 2.0 will drop support for some Python versions, and if you're using internal APIs then as usual that may break without warning). 

 It does have two new features:
<dl>
<dt>&bull;
<dd> New @seed() decorator which allows you to manually seed a test. This may be harmlessly combined with and overrides the derandomize setting.
<dt>&bull;
<dd> settings objects may now be used as a decorator to fix those settings to a particular @given test. 

 API changes (old usage still works but is deprecated):
<dt>&bull;
<dd> Settings has been renamed to settings (lower casing) in order to make the decorator usage more natural.
<dt>&bull;
<dd> Functions for the storage directory that were in hypothesis.settings are now in a new hypothesis.configuration module. 

 Additional deprecations:
<dt>&bull;
<dd> the average_list_length setting has been deprecated in favour of being explicit.
<dt>&bull;
<dd> the basic() strategy has been deprecated as it is impossible to support it under a Conjecture based model, which will hopefully be implemented at some point in the 2.x series.
<dt>&bull;
<dd> the n_ary_tree strategy (which was never actually part of the public API) has been deprecated.
<dt>&bull;
<dd> Passing settings or random as keyword arguments to given is deprecated (use the new functionality instead) 

 Bug fixes:
<dt>&bull;
<dd> No longer emit PendingDeprecationWarning for __iter__ and StopIteration in streaming() values.
<dt>&bull;
<dd> When running in health check mode with non strict, don't print quite so many errors for an exception in reify.
<dt>&bull;
<dd> When an assumption made in a test or a filter is flaky, tests will now raise Flaky instead of UnsatisfiedAssumption.</dl>

<h3><i>1.18.1</i> - 2015-12-22</h3>

 

 Two behind the scenes changes:
<dl>
<dt>&bull;
<dd> Hypothesis will no longer write generated code to the file system. This will improve performance on some systems (e.g. if you're using <i>PythonAnywhere</i> which is running your code from NFS) and prevent some annoying interactions with auto-restarting systems.
<dt>&bull;
<dd> Hypothesis will cache the creation of some strategies. This can significantly improve performance for code that uses flatmap or composite and thus has to instantiate strategies a lot.</dl>

<h3><i>1.18.0</i> - 2015-12-21</h3>

 

 Features:
<dl>
<dt>&bull;
<dd> Tests and find are now explicitly seeded off the global random module. This means that if you nest one inside the other you will now get a health check error. It also means that you can control global randomization by seeding random.
<dt>&bull;
<dd> There is a new random_module() strategy which seeds the global random module for you and handles things so that you don't get a health check warning if you use it inside your tests.
<dt>&bull;
<dd> floats() now accepts two new arguments: allow_nan and allow_infinity. These default to the old behaviour, but when set to False will do what the names suggest. 

 Bug fixes:
<dt>&bull;
<dd> Fix a bug where tests that used text() on Python 3.4+ would not actually be deterministic even when explicitly seeded or using the derandomize mode, because generation depended on dictionary iteration order which was affected by hash randomization.
<dt>&bull;
<dd> Fix a bug where with complicated strategies the timing of the initial health check could affect the seeding of the subsequent test, which would also render supposedly deterministic tests non-deterministic in some scenarios.
<dt>&bull;
<dd> In some circumstances flatmap() could get confused by two structurally similar things it could generate and would produce a flaky test where the first time it produced an error but the second time it produced the other value, which was not an error. The same bug was presumably also possible in composite().
<dt>&bull;
<dd> flatmap() and composite() initial generation should now be moderately faster. This will be particularly noticeable when you have many values drawn from the same strategy in a single run, e.g. constructs like lists(s.flatmap(f)). Shrinking performance <i>may</i> have suffered, but this didn't actually produce an interestingly worse result in any of the standard scenarios tested.</dl>

<h3><i>1.17.1</i> - 2015-12-16</h3>

 

 A small bug fix release, which fixes the fact that the 'note' function could not be used on tests which used the @example decorator to provide explicit examples.

<h3><i>1.17.0</i> - 2015-12-15</h3>

 

 This is actually the same release as 1.16.1, but 1.16.1 has been pulled because it contains the following additional change that was not intended to be in a patch release (it's perfectly stable, but is a larger change that should have required a minor version bump):
<dl>
<dt>&bull;
<dd> Hypothesis will now perform a series of &quot;health checks&quot; as part of running your tests. These detect and warn about some common error conditions that people often run into which wouldn't necessarily have caused the test to fail but would cause e.g. degraded performance or confusing results.</dl>

<h3><i>1.16.1</i> - 2015-12-14</h3>

 

 Note: This release has been removed. 

 A small bugfix release that allows bdists for Hypothesis to be built under 2.7 - the compat3.py file which had Python 3 syntax wasn't intended to be loaded under Python 2, but when building a bdist it was. In particular this would break running setup.py test.

<h3><i>1.16.0</i> - 2015-12-08</h3>

 

 There are no public API changes in this release but it includes a behaviour change that I wasn't comfortable putting in a patch release.
<dl>
<dt>&bull;
<dd> Functions from hypothesis.strategies will no longer raise InvalidArgument on bad arguments. Instead the same errors will be raised when a test using such a strategy is run. This may improve startup time in some cases, but the main reason for it is so that errors in strategies won't cause errors in loading, and it can interact correctly with things like pytest.mark.skipif.
<dt>&bull;
<dd> Errors caused by accidentally invoking the legacy API are now much less confusing, although still throw NotImplementedError.
<dt>&bull;
<dd> hypothesis.extra.django is 1.9 compatible.
<dt>&bull;
<dd> When tests are run with max_shrinks=0 this will now still rerun the test on failure and will no longer print &quot;Trying example:&quot; before each run. Additionally note() will now work correctly when used with max_shrinks=0.</dl>

<h3><i>1.15.0</i> - 2015-11-24</h3>

 

 A release with two new features.
<dl>
<dt>&bull;
<dd> A 'characters' strategy for more flexible generation of text with particular character ranges and types, kindly contributed by <i>Alexander Shorin</i>.
<dt>&bull;
<dd> Add support for preconditions to the rule based stateful testing. Kindly contributed by <i>Christopher Armstrong</i></dl>

<h3><i>1.14.0</i> - 2015-11-01</h3>

 

 New features:
<dl>
<dt>&bull;
<dd> Add 'note' function which lets you include additional information in the final test run's output.
<dt>&bull;
<dd> Add 'choices' strategy which gives you a choice function that emulates random.choice.
<dt>&bull;
<dd> Add 'uuid' strategy that generates UUIDs'
<dt>&bull;
<dd> Add 'shared' strategy that lets you create a strategy that just generates a single shared value for each test run 

 Bugs:
<dt>&bull;
<dd> Using strategies of the form streaming(x.flatmap(f)) with find or in stateful testing would have caused InvalidArgument errors when the resulting values were used (because code that expected to only be called within a test context would be invoked).</dl>

<h3><i>1.13.0</i> - 2015-10-29</h3>

 

 This is quite a small release, but deprecates some public API functions and removes some internal API functionality so gets a minor version bump.
<dl>
<dt>&bull;
<dd> All calls to the 'strategy' function are now deprecated, even ones which pass just a SearchStrategy instance (which is still a no-op).
<dt>&bull;
<dd> Never documented hypothesis.extra entry_points mechanism has now been removed ( it was previously how hypothesis.extra packages were loaded and has been deprecated and unused for some time)
<dt>&bull;
<dd> Some corner cases that could previously have produced an OverflowError when simplifying failing cases using hypothesis.extra.datetimes (or dates or times) have now been fixed.
<dt>&bull;
<dd> Hypothesis load time for first import has been significantly reduced - it used to be around 250ms (on my SSD laptop) and now is around 100-150ms. This almost never matters but was slightly annoying when using it in the console.
<dt>&bull;
<dd> hypothesis.strategies.randoms was previously missing from __all__.</dl>

<h3><i>1.12.0</i> - 2015-10-18</h3>

<dl>
<dt>&bull;
<dd> Significantly improved performance of creating strategies using the functions from the hypothesis.strategies module by deferring the calculation of their repr until it was needed. This is unlikely to have been an performance issue for you unless you were using flatmap, composite or stateful testing, but for some cases it could be quite a significant impact.
<dt>&bull;
<dd> A number of cases where the repr of strategies build from lambdas is improved
<dt>&bull;
<dd> Add dates() and times() strategies to hypothesis.extra.datetimes
<dt>&bull;
<dd> Add new 'profiles' mechanism to the settings system
<dt>&bull;
<dd> Deprecates mutability of Settings, both the Settings.default top level property and individual settings.
<dt>&bull;
<dd> A Settings object may now be directly initialized from a parent Settings.
<dt>&bull;
<dd> @given should now give a better error message if you attempt to use it with a function that uses destructuring arguments (it still won't work, but it will error more clearly),
<dt>&bull;
<dd> A number of spelling corrections in error messages
<dt>&bull;
<dd> py.test should no longer display the intermediate modules Hypothesis generates when running in verbose mode
<dt>&bull;
<dd> Hypothesis should now correctly handle printing objects with non-ascii reprs on python 3 when running in a locale that cannot handle ascii printing to stdout.
<dt>&bull;
<dd> Add a unique=True argument to lists(). This is equivalent to unique_by=lambda x: x, but offers a more convenient syntax.</dl>

<h3><i>1.11.4</i> - 2015-09-27</h3>

<dl>
<dt>&bull;
<dd> Hide modifications Hypothesis needs to make to sys.path by undoing them after we've imported the relevant modules. This is a workaround for issues cryptography experienced on windows.
<dt>&bull;
<dd> Slightly improved performance of drawing from sampled_from on large lists of alternatives.
<dt>&bull;
<dd> Significantly improved performance of drawing from one_of or strategies using | (note this includes a lot of strategies internally - floats() and integers() both fall into this category). There turned out to be a massive performance regression introduced in 1.10.0 affecting these which probably would have made tests using Hypothesis significantly slower than they should have been.</dl>

<h3><i>1.11.3</i> - 2015-09-23</h3>

<dl>
<dt>&bull;
<dd> Better argument validation for datetimes() strategy - previously setting max_year &lt; datetime.MIN_YEAR or min_year &gt; datetime.MAX_YEAR would not have raised an InvalidArgument error and instead would have behaved confusingly.
<dt>&bull;
<dd> Compatibility with being run on pytest &lt; 2.7 (achieved by disabling the plugin).</dl>

<h3><i>1.11.2</i> - 2015-09-23</h3>

 

 Bug fixes:
<dl>
<dt>&bull;
<dd> Settings(database=my_db) would not be correctly inherited when used as a default setting, so that newly created settings would use the database_file setting and create an SQLite example database.
<dt>&bull;
<dd> Settings.default.database = my_db would previously have raised an error and now works.
<dt>&bull;
<dd> Timeout could sometimes be significantly exceeded if during simplification there were a lot of examples tried that didn't trigger the bug.
<dt>&bull;
<dd> When loading a heavily simplified example using a basic() strategy from the database this could cause Python to trigger a recursion error.
<dt>&bull;
<dd> Remove use of deprecated API in pytest plugin so as to not emit warning 

 Misc:
<dt>&bull;
<dd> hypothesis-pytest is now part of hypothesis core. This should have no externally visible consequences, but you should update your dependencies to remove hypothesis-pytest and depend on only Hypothesis.
<dt>&bull;
<dd> Better repr for hypothesis.extra.datetimes() strategies.
<dt>&bull;
<dd> Add .close() method to abstract base class for Backend (it was already present in the main implementation).</dl>

<h3><i>1.11.1</i> - 2015-09-16</h3>

 

 Bug fixes:
<dl>
<dt>&bull;
<dd> When running Hypothesis tests in parallel (e.g. using pytest-xdist) there was a race condition caused by code generation.
<dt>&bull;
<dd> Example databases are now cached per thread so as to not use sqlite connections from multiple threads. This should make Hypothesis now entirely thread safe.
<dt>&bull;
<dd> floats() with only min_value or max_value set would have had a very bad distribution.
<dt>&bull;
<dd> Running on 3.5, Hypothesis would have emitted deprecation warnings because of use of inspect.getargspec</dl>

<h3><i>1.11.0</i> - 2015-08-31</h3>

<dl>
<dt>&bull;
<dd> text() with a non-string alphabet would have used the repr() of the the alphabet instead of its contexts. This is obviously silly. It now works with any sequence of things convertible to unicode strings.
<dt>&bull;
<dd> @given will now work on methods whose definitions contains no explicit positional arguments, only varargs (<i>bug #118</i>). This may have some knock on effects because it means that @given no longer changes the argspec of functions other than by adding defaults.
<dt>&bull;
<dd> Introduction of new @composite feature for more natural definition of strategies you'd previously have used flatmap for.</dl>

<h3><i>1.10.6</i> - 2015-08-26</h3>

 

 Fix support for fixtures on Django 1.7.

<h3>1.10.4 - 2015-08-21</h3>

 

 Tiny bug fix release:
<dl>
<dt>&bull;
<dd> If the database_file setting is set to None, this would have resulted in an error when running tests. Now it does the same as setting database to None.</dl>

<h3><i>1.10.3</i> - 2015-08-19</h3>

 

 Another small bug fix release.
<dl>
<dt>&bull;
<dd> lists(elements, unique_by=some_function, min_size=n) would have raised a ValidationError if n &gt; Settings.default.average_list_length because it would have wanted to use an average list length shorter than the minimum size of the list, which is impossible. Now it instead defaults to twice the minimum size in these circumstances.
<dt>&bull;
<dd> basic() strategy would have only ever produced at most ten distinct values per run of the test (which is bad if you e.g. have it inside a list). This was obviously silly. It will now produce a much better distribution of data, both duplicated and non duplicated.</dl>

<h3><i>1.10.2</i> - 2015-08-19</h3>

 

 This is a small bug fix release:
<dl>
<dt>&bull;
<dd> star imports from hypothesis should now work correctly.
<dt>&bull;
<dd> example quality for examples using flatmap will be better, as the way it had previously been implemented was causing problems where Hypothesis was erroneously labelling some examples as being duplicates.</dl>

<h3><i>1.10.0</i> - 2015-08-04</h3>

 

 This is just a bugfix and performance release, but it changes some semi-public APIs, hence the minor version bump.
<dl>
<dt>&bull;
<dd> Significant performance improvements for strategies which are one_of() many branches. In particular this included recursive() strategies. This should take the case where you use one recursive() strategy as the base strategy of another from unusably slow (tens of seconds per generated example) to reasonably fast.
<dt>&bull;
<dd> Better handling of just() and sampled_from() for values which have an incorrect __repr__ implementation that returns non-ASCII unicode on Python 2.
<dt>&bull;
<dd> Better performance for flatmap from changing the internal morpher API to be significantly less general purpose.
<dt>&bull;
<dd> Introduce a new semi-public BuildContext/cleanup API. This allows strategies to register cleanup activities that should run once the example is complete. Note that this will interact somewhat weirdly with find.
<dt>&bull;
<dd> Better simplification behaviour for streaming strategies.
<dt>&bull;
<dd> Don't error on lambdas which use destructuring arguments in Python 2.
<dt>&bull;
<dd> Add some better reprs for a few strategies that were missing good ones.
<dt>&bull;
<dd> The Random instances provided by randoms() are now copyable.
<dt>&bull;
<dd> Slightly more debugging information about simplify when using a debug verbosity level.
<dt>&bull;
<dd> Support using given for functions with varargs, but not passing arguments to it as positional.</dl>

<h3><i>1.9.0</i> - 2015-07-27</h3>

 

 Codename: The great bundling. 

 This release contains two fairly major changes. 

 The first is the deprecation of the hypothesis-extra mechanism. From now on all the packages that were previously bundled under it other than hypothesis-pytest (which is a different beast and will remain separate). The functionality remains unchanged and you can still import them from exactly the same location, they just are no longer separate packages. 

 The second is that this introduces a new way of building strategies which lets you build up strategies recursively from other strategies. 

 It also contains the minor change that calling .example() on a strategy object will give you examples that are more representative of the actual data you'll get. There used to be some logic in there to make the examples artificially simple but this proved to be a bad idea.

<h3><i>1.8.5</i> - 2015-07-24</h3>

 

 This contains no functionality changes but fixes a mistake made with building the previous package that would have broken installation on Windows.

<h3><i>1.8.4</i> - 2015-07-20</h3>

 

 Bugs fixed:
<dl>
<dt>&bull;
<dd> When a call to floats() had endpoints which were not floats but merely convertible to one (e.g. integers), these would be included in the generated data which would cause it to generate non-floats.
<dt>&bull;
<dd> Splitting lambdas used in the definition of flatmap, map or filter over multiple lines would break the repr, which would in turn break their usage.</dl>

<h3><i>1.8.3</i> - 2015-07-20</h3>

 

 &quot;Falsifying example&quot; would not have been printed when the failure came from an explicit example.

<h3><i>1.8.2</i> - 2015-07-18</h3>

 

 Another small bugfix release:
<dl>
<dt>&bull;
<dd> When using ForkingTestCase you would usually not get the falsifying example printed if the process exited abnormally (e.g. due to os._exit).
<dt>&bull;
<dd> Improvements to the distribution of characters when using text() with a default alphabet. In particular produces a better distribution of ascii and whitespace in the alphabet.</dl>

<h3>1.8.1 - 2015-07-17</h3>

 

 This is a small release that contains a workaround for people who have bad reprs returning non ascii text on Python 2.7. This is not a bug fix for Hypothesis per se because that's not a thing that is actually supposed to work, but Hypothesis leans more heavily on repr than is typical so it's worth having a workaround for.

<h3><i>1.8.0</i> - 2015-07-16</h3>

 

 New features:
<dl>
<dt>&bull;
<dd> Much more sensible reprs for strategies, especially ones that come from hypothesis.strategies. These should now have as reprs python code that would produce the same strategy.
<dt>&bull;
<dd> lists() accepts a unique_by argument which forces the generated lists to be only contain elements unique according to some function key (which must return a hashable value).
<dt>&bull;
<dd> Better error messages from flaky tests to help you debug things. 

 Mostly invisible implementation details that may result in finding new bugs in your code:
<dt>&bull;
<dd> Sets and dictionary generation should now produce a better range of results.
<dt>&bull;
<dd> floats with bounds now focus more on 'critical values', trying to produce values at edge cases.
<dt>&bull;
<dd> flatmap should now have better simplification for complicated cases, as well as generally being (I hope) more reliable. 

 Bug fixes:
<dt>&bull;
<dd> You could not previously use assume() if you were using the forking executor.</dl>

<h3><i>1.7.2</i> - 2015-07-10</h3>

 

 This is purely a bug fix release:
<dl>
<dt>&bull;
<dd> When using floats() with stale data in the database you could sometimes get values in your tests that did not respect min_value or max_value.
<dt>&bull;
<dd> When getting a Flaky error from an unreliable test it would have incorrectly displayed the example that caused it.
<dt>&bull;
<dd> 2.6 dependency on backports was incorrectly specified. This would only have caused you problems if you were building a universal wheel from Hypothesis, which is not how Hypothesis ships, so unless you're explicitly building wheels for your dependencies and support Python 2.6 plus a later version of Python this probably would never have affected you.
<dt>&bull;
<dd> If you use flatmap in a way that the strategy on the right hand side depends sensitively on the left hand side you may have occasionally seen Flaky errors caused by producing unreliable examples when minimizing a bug. This use case may still be somewhat fraught to be honest. This code is due a major rearchitecture for 1.8, but in the meantime this release fixes the only source of this error that I'm aware of.</dl>

<h3><i>1.7.1</i> - 2015-06-29</h3>

 

 Codename: There is no 1.7.0. 

 A slight technical hitch with a premature upload means there's was a yanked 1.7.0 release. Oops. 

 The major feature of this release is Python 2.6 support. Thanks to Jeff Meadows for doing most of the work there. 

 Other minor features
<dl>
<dt>&bull;
<dd> strategies now has a permutations() function which returns a strategy yielding permutations of values from a given collection.
<dt>&bull;
<dd> if you have a flaky test it will print the exception that it last saw before failing with Flaky, even if you do not have verbose reporting on.
<dt>&bull;
<dd> Slightly experimental git merge script available as &quot;python -m hypothesis.tools.mergedbs&quot;. Instructions on how to use it in the docstring of that file. 

 Bug fixes:
<dt>&bull;
<dd> Better performance from use of filter. In particular tests which involve large numbers of heavily filtered strategies should perform a lot better.
<dt>&bull;
<dd> floats() with a negative min_value would not have worked correctly (worryingly, it would have just silently failed to run any examples). This is now fixed.
<dt>&bull;
<dd> tests using sampled_from would error if the number of sampled elements was smaller than min_satisfying_examples.</dl>

<h3>1.6.2 - 2015-06-08</h3>

 

 This is just a few small bug fixes:
<dl>
<dt>&bull;
<dd> Size bounds were not validated for values for a binary() strategy when reading examples from the database.
<dt>&bull;
<dd> sampled_from is now in __all__ in hypothesis.strategies
<dt>&bull;
<dd> floats no longer consider negative integers to be simpler than positive non-integers
<dt>&bull;
<dd> Small floating point intervals now correctly count members, so if you have a floating point interval so narrow there are only a handful of values in it, this will no longer cause an error when Hypothesis runs out of values.</dl>

<h3>1.6.1 - 2015-05-21</h3>

 

 This is a small patch release that fixes a bug where 1.6.0 broke the use of flatmap with the deprecated API and assumed the passed in function returned a SearchStrategy instance rather than converting it to a strategy.

<h3><i>1.6.0</i> - 2015-05-21</h3>

 

 This is a smallish release designed to fix a number of bugs and smooth out some weird behaviours.
<dl>
<dt>&bull;
<dd> Fix a critical bug in flatmap where it would reuse old strategies. If all your flatmap code was pure you're fine. If it's not, I'm surprised it's working at all. In particular if you want to use flatmap with django models, you desperately need to upgrade to this version.
<dt>&bull;
<dd> flatmap simplification performance should now be better in some cases where it previously had to redo work.
<dt>&bull;
<dd> Fix for a bug where invalid unicode data with surrogates could be generated during simplification (it was already filtered out during actual generation).
<dt>&bull;
<dd> The Hypothesis database is now keyed off the name of the test instead of the type of data. This makes much more sense now with the new strategies API and is generally more robust. This means you will lose old examples on upgrade.
<dt>&bull;
<dd> The database will now not delete values which fail to deserialize correctly, just skip them. This is to handle cases where multiple incompatible strategies share the same key.
<dt>&bull;
<dd> find now also saves and loads values from the database, keyed off a hash of the function you're finding from.
<dt>&bull;
<dd> Stateful tests now serialize and load values from the database. They should have before, really. This was a bug.
<dt>&bull;
<dd> Passing a different verbosity level into a test would not have worked entirely correctly, leaving off some messages. This is now fixed.
<dt>&bull;
<dd> Fix a bug where derandomized tests with unicode characters in the function body would error on Python 2.7.</dl>

<h3><i>1.5.0</i> - 2015-05-14</h3>

 

 Codename: Strategic withdrawal. 

 The purpose of this release is a radical simplification of the API for building strategies. Instead of the old approach of @strategy.extend and things that get converted to strategies, you just build strategies directly. 

 The old method of defining strategies will still work until Hypothesis 2.0, because it's a major breaking change, but will now emit deprecation warnings. 

 The new API is also a lot more powerful as the functions for defining strategies give you a lot of dials to turn. See <b>the updated data section</b> for details. 

 Other changes:
<dl>
<dt>&bull;
<dd> Mixing keyword and positional arguments in a call to @given is deprecated as well.
<dt>&bull;
<dd> There is a new setting called 'strict'. When set to True, Hypothesis will raise warnings instead of merely printing them. Turning it on by default is inadvisable because it means that Hypothesis minor releases can break your code, but it may be useful for making sure you catch all uses of deprecated APIs.
<dt>&bull;
<dd> max_examples in settings is now interpreted as meaning the maximum number of unique (ish) examples satisfying assumptions. A new setting max_iterations which defaults to a larger value has the old interpretation.
<dt>&bull;
<dd> Example generation should be significantly faster due to a new faster parameter selection algorithm. This will mostly show up for simple data types - for complex ones the parameter selection is almost certainly dominated.
<dt>&bull;
<dd> Simplification has some new heuristics that will tend to cut down on cases where it could previously take a very long time.
<dt>&bull;
<dd> timeout would previously not have been respected in cases where there were a lot of duplicate examples. You probably wouldn't have previously noticed this because max_examples counted duplicates, so this was very hard to hit in a way that mattered.
<dt>&bull;
<dd> A number of internal simplifications to the SearchStrategy API.
<dt>&bull;
<dd> You can now access the current Hypothesis version as hypothesis.__version__.
<dt>&bull;
<dd> A top level function is provided for running the stateful tests without the TestCase infrastructure.</dl>

<h3><i>1.4.0</i> - 2015-05-04</h3>

 

 Codename: What a state. 

 The <i>big</i> feature of this release is the new and slightly experimental stateful testing API. You can read more about that in <b>the appropriate section</b>. 

 Two minor features the were driven out in the course of developing this:
<dl>
<dt>&bull;
<dd> You can now set settings.max_shrinks to limit the number of times Hypothesis will try to shrink arguments to your test. If this is set to &lt;= 0 then Hypothesis will not rerun your test and will just raise the failure directly. Note that due to technical limitations if max_shrinks is &lt;= 0 then Hypothesis will print <i>every</i> example it calls your test with rather than just the failing one. Note also that I don't consider settings max_shrinks to zero a sensible way to run your tests and it should really be considered a debug feature.
<dt>&bull;
<dd> There is a new debug level of verbosity which is even <i>more</i> verbose than verbose. You probably don't want this. 

 Breakage of semi-public SearchStrategy API:
<dt>&bull;
<dd> It is now a required invariant of SearchStrategy that if u simplifies to v then it is not the case that strictly_simpler(u, v). i.e. simplifying should not <i>increase</i> the complexity even though it is not required to decrease it. Enforcing this invariant lead to finding some bugs where simplifying of integers, floats and sets was suboptimal.
<dt>&bull;
<dd> Integers in basic data are now required to fit into 64 bits. As a result python integer types are now serialized as strings, and some types have stopped using quite so needlessly large random seeds. 

 Hypothesis Stateful testing was then turned upon Hypothesis itself, which lead to an amazing number of minor bugs being found in Hypothesis itself. 

 Bugs fixed (most but not all from the result of stateful testing) include:
<dt>&bull;
<dd> Serialization of streaming examples was flaky in a way that you would probably never notice: If you generate a template, simplify it, serialize it, deserialize it, serialize it again and then deserialize it you would get the original stream instead of the simplified one.
<dt>&bull;
<dd> If you reduced max_examples below the number of examples already saved in the database, you would have got a ValueError. Additionally, if you had more than max_examples in the database all of them would have been considered.
<dt>&bull;
<dd> @given will no longer count duplicate examples (which it never called your function with) towards max_examples. This may result in your tests running slower, but that's probably just because they're trying more examples.
<dt>&bull;
<dd> General improvements to example search which should result in better performance and higher quality examples. In particular parameters which have a history of producing useless results will be more aggressively culled. This is useful both because it decreases the chance of useless examples and also because it's much faster to not check parameters which we were unlikely to ever pick!
<dt>&bull;
<dd> integers_from and lists of types with only one value (e.g. [None]) would previously have had a very high duplication rate so you were probably only getting a handful of examples. They now have a much lower duplication rate, as well as the improvements to search making this less of a problem in the first place.
<dt>&bull;
<dd> You would sometimes see simplification taking significantly longer than your defined timeout. This would happen because timeout was only being checked after each <i>successful</i> simplification, so if Hypothesis was spending a lot of time unsuccessfully simplifying things it wouldn't stop in time. The timeout is now applied for unsuccessful simplifications too.
<dt>&bull;
<dd> In Python 2.7, integers_from strategies would have failed during simplification with an OverflowError if their starting point was at or near to the maximum size of a 64-bit integer.
<dt>&bull;
<dd> flatmap and map would have failed if called with a function without a __name__ attribute.
<dt>&bull;
<dd> If max_examples was less than min_satisfying_examples this would always error. Now min_satisfying_examples is capped to max_examples. Note that if you have assumptions to satisfy here this will still cause an error. 

 Some minor quality improvements:
<dt>&bull;
<dd> Lists of streams, flatmapped strategies and basic strategies should now now have slightly better simplification.</dl>

<h3><i>1.3.0</i> - 2015-05-22</h3>

 

 New features:
<dl>
<dt>&bull;
<dd> New verbosity level API for printing intermediate results and exceptions.
<dt>&bull;
<dd> New specifier for strings generated from a specified alphabet.
<dt>&bull;
<dd> Better error messages for tests that are failing because of a lack of enough examples. 

 Bug fixes:
<dt>&bull;
<dd> Fix error where use of ForkingTestCase would sometimes result in too many open files.
<dt>&bull;
<dd> Fix error where saving a failing example that used flatmap could error.
<dt>&bull;
<dd> Implement simplification for sampled_from, which apparently never supported it previously. Oops. 

 General improvements:
<dt>&bull;
<dd> Better range of examples when using one_of or sampled_from.
<dt>&bull;
<dd> Fix some pathological performance issues when simplifying lists of complex values.
<dt>&bull;
<dd> Fix some pathological performance issues when simplifying examples that require unicode strings with high codepoints.
<dt>&bull;
<dd> Random will now simplify to more readable examples.</dl>

<h3><i>1.2.1</i> - 2015-04-16</h3>

 

 A small patch release for a bug in the new executors feature. Tests which require doing something to their result in order to fail would have instead reported as flaky.

<h3><i>1.2.0</i> - 2015-04-15</h3>

 

 Codename: Finders keepers. 

 A bunch of new features and improvements.
<dl>
<dt>&bull;
<dd> Provide a mechanism for customizing how your tests are executed.
<dt>&bull;
<dd> Provide a test runner that forks before running each example. This allows better support for testing native code which might trigger a segfault or a C level assertion failure.
<dt>&bull;
<dd> Support for using Hypothesis to find examples directly rather than as just as a test runner.
<dt>&bull;
<dd> New streaming type which lets you generate infinite lazily loaded streams of data - perfect for if you need a number of examples but don't know how many.
<dt>&bull;
<dd> Better support for large integer ranges. You can now use integers_in_range with ranges of basically any size. Previously large ranges would have eaten up all your memory and taken forever.
<dt>&bull;
<dd> Integers produce a wider range of data than before - previously they would only rarely produce integers which didn't fit into a machine word. Now it's much more common. This percolates to other numeric types which build on integers.
<dt>&bull;
<dd> Better validation of arguments to @given. Some situations that would previously have caused silently wrong behaviour will now raise an error.
<dt>&bull;
<dd> Include +/- sys.float_info.max in the set of floating point edge cases that Hypothesis specifically tries.
<dt>&bull;
<dd> Fix some bugs in floating point ranges which happen when given +/- sys.float_info.max as one of the endpoints... (really any two floats that are sufficiently far apart so that x, y are finite but y - x is infinite). This would have resulted in generating infinite values instead of ones inside the range.</dl>

<h3><i>1.1.1</i> - 2015-04-07</h3>

 

 Codename: Nothing to see here 

 This is just a patch release put out because it fixed some internal bugs that would block the Django integration release but did not actually affect anything anyone could previously have been using. It also contained a minor quality fix for floats that I'd happened to have finished in time.
<dl>
<dt>&bull;
<dd> Fix some internal bugs with object lifecycle management that were impossible to hit with the previously released versions but broke hypothesis-django.
<dt>&bull;
<dd> Bias floating point numbers somewhat less aggressively towards very small numbers</dl>

<h3><i>1.1.0</i> - 2015-04-06</h3>

 

 Codename: No-one mention the M word.
<dl>
<dt>&bull;
<dd> Unicode strings are more strongly biased towards ascii characters. Previously they would generate all over the space. This is mostly so that people who try to shape their unicode strings with assume() have less of a bad time.
<dt>&bull;
<dd> A number of fixes to data deserialization code that could theoretically have caused mysterious bugs when using an old version of a Hypothesis example database with a newer version. To the best of my knowledge a change that could have triggered this bug has never actually been seen in the wild. Certainly no-one ever reported a bug of this nature.
<dt>&bull;
<dd> Out of the box support for Decimal and Fraction.
<dt>&bull;
<dd> new dictionary specifier for dictionaries with variable keys.
<dt>&bull;
<dd> Significantly faster and higher quality simplification, especially for collections of data.
<dt>&bull;
<dd> New filter() and flatmap() methods on Strategy for better ways of building strategies out of other strategies.
<dt>&bull;
<dd> New BasicStrategy class which allows you to define your own strategies from scratch without needing an existing matching strategy or being exposed to the full horror or non-public nature of the SearchStrategy interface.</dl>

<h3><i>1.0.0</i> - 2015-03-27</h3>

 

 Codename: Blast-off! 

 There are no code changes in this release. This is precisely the 0.9.2 release with some updated documentation.

<h3>0.9.2 - 2015-03-26</h3>

 

 Codename: T-1 days.
<dl>
<dt>&bull;
<dd> floats_in_range would not actually have produced floats_in_range unless that range happened to be (0, 1). Fix this.</dl>

<h3>0.9.1 - 2015-03-25</h3>

 

 Codename: T-2 days.
<dl>
<dt>&bull;
<dd> Fix a bug where if you defined a strategy using map on a lambda then the results would not be saved in the database.
<dt>&bull;
<dd> Significant performance improvements when simplifying examples using lists, strings or bounded integer ranges.</dl>

<h3>0.9.0 - 2015-03-23</h3>

 

 Codename: The final countdown 

 This release could also be called 1.0-RC1. 

 It contains a teeny tiny bugfix, but the real point of this release is to declare feature freeze. There will be zero functionality changes between 0.9.0 and 1.0 unless something goes really really wrong. No new features will be added, no breaking API changes will occur, etc. This is the final shakedown before I declare Hypothesis stable and ready to use and throw a party to celebrate. 

 Bug bounty for any bugs found between now and 1.0: I will buy you a drink (alcoholic, caffeinated, or otherwise) and shake your hand should we ever find ourselves in the same city at the same time. 

 The one tiny bugfix:
<dl>
<dt>&bull;
<dd> Under pypy, databases would fail to close correctly when garbage collected, leading to a memory leak and a confusing error message if you were repeatedly creating databases and not closing them. It is very unlikely you were doing this and the chances of you ever having noticed this bug are very low.</dl>

<h3>0.7.2 - 2015-03-22</h3>

 

 Codename: Hygienic macros or bust
<dl>
<dt>&bull;
<dd> You can now name an argument to @given 'f' and it won't break (issue #38)
<dt>&bull;
<dd> strategy_test_suite is now named strategy_test_suite as the documentation claims and not in fact strategy_test_suitee
<dt>&bull;
<dd> Settings objects can now be used as a context manager to temporarily override the default values inside their context.</dl>

<h3>0.7.1 - 2015-03-21</h3>

 

 Codename: Point releases go faster
<dl>
<dt>&bull;
<dd> Better string generation by parametrizing by a limited alphabet
<dt>&bull;
<dd> Faster string simplification - previously if simplifying a string with high range unicode characters it would try every unicode character smaller than that. This was pretty pointless. Now it stops after it's a short range (it can still reach smaller ones through recursive calls because of other simplifying operations).
<dt>&bull;
<dd> Faster list simplification by first trying a binary chop down the middle
<dt>&bull;
<dd> Simultaneous simplification of identical elements in a list. So if a bug only triggers when you have duplicates but you drew e.g. [-17, -17], this will now simplify to [0, 0].</dl>

<h3>0.7.0, - 2015-03-20</h3>

 

 Codename: Starting to look suspiciously real 

 This is probably the last minor release prior to 1.0. It consists of stability improvements, a few usability things designed to make Hypothesis easier to try out, and filing off some final rough edges from the API.
<dl>
<dt>&bull;
<dd> Significant speed and memory usage improvements
<dt>&bull;
<dd> Add an example() method to strategy objects to give an example of the sort of data that the strategy generates.
<dt>&bull;
<dd> Remove .descriptor attribute of strategies
<dt>&bull;
<dd> Rename descriptor_test_suite to strategy_test_suite
<dt>&bull;
<dd> Rename the few remaining uses of descriptor to specifier (descriptor already has a defined meaning in Python)</dl>

<h3>0.6.0 - 2015-03-13</h3>

 

 Codename: I'm sorry, were you using that API? 

 This is primarily a &quot;simplify all the weird bits of the API&quot; release. As a result there are a lot of breaking changes. If you just use @given with core types then you're probably fine. 

 In particular:
<dl>
<dt>&bull;
<dd> Stateful testing has been removed from the API
<dt>&bull;
<dd> The way the database is used has been rendered less useful (sorry). The feature for reassembling values saved from other tests doesn't currently work. This will probably be brought back in post 1.0.
<dt>&bull;
<dd> SpecificationMapper is no longer a thing. Instead there is an ExtMethod called strategy which you extend to specify how to convert other types to strategies.
<dt>&bull;
<dd> Settings are now extensible so you can add your own for configuring a strategy
<dt>&bull;
<dd> MappedSearchStrategy no longer needs an unpack method
<dt>&bull;
<dd> Basically all the SearchStrategy internals have changed massively. If you implemented SearchStrategy directly rather than using MappedSearchStrategy talk to me about fixing it.
<dt>&bull;
<dd> Change to the way extra packages work. You now specify the package. This must have a load() method. Additionally any modules in the package will be loaded in under hypothesis.extra 

 Bug fixes:
<dt>&bull;
<dd> Fix for a bug where calling falsify on a lambda with a non-ascii character in its body would error. 

 Hypothesis Extra:
<dt><b>hypothesis-fakefactory: An extension for using faker data in hypothesis. Depends</b>
<dd> on fake-factory.</dl>

<h3>0.5.0 - 2015-02-10</h3>

 

 Codename: Read all about it. 

 Core hypothesis:
<dl>
<dt>&bull;
<dd> Add support back in for pypy and python 3.2
<dt>&bull;
<dd> @given functions can now be invoked with some arguments explicitly provided. If all arguments that hypothesis would have provided are passed in then no falsification is run.
<dt>&bull;
<dd> Related to the above, this means that you can now use pytest fixtures and mark.parametrize with Hypothesis without either interfering with the other.
<dt>&bull;
<dd> Breaking change: @given no longer works for functions with varargs (varkwargs are fine). This might be added back in at a later date.
<dt>&bull;
<dd> Windows is now fully supported. A limited version (just the tests with none of the extras) of the test suite is run on windows with each commit so it is now a first class citizen of the Hypothesis world.
<dt>&bull;
<dd> Fix a bug for fuzzy equality of equal complex numbers with different reprs (this can happen when one coordinate is zero). This shouldn't affect users - that feature isn't used anywhere public facing.
<dt>&bull;
<dd> Fix generation of floats on windows and 32-bit builds of python. I was using some struct.pack logic that only worked on certain word sizes.
<dt>&bull;
<dd> When a test times out and hasn't produced enough examples this now raises a Timeout subclass of Unfalsifiable.
<dt>&bull;
<dd> Small search spaces are better supported. Previously something like a @given(bool, bool) would have failed because it couldn't find enough examples. Hypothesis is now aware of the fact that these are small search spaces and will not error in this case.
<dt>&bull;
<dd> Improvements to parameter search in the case of hard to satisfy assume. Hypothesis will now spend less time exploring parameters that are unlikely to provide anything useful.
<dt>&bull;
<dd> Increase chance of generating &quot;nasty&quot; floats
<dt>&bull;
<dd> Fix a bug that would have caused unicode warnings if you had a sampled_from that was mixing unicode and byte strings.
<dt>&bull;
<dd> Added a standard test suite that you can use to validate a custom strategy you've defined is working correctly. 

 Hypothesis extra: 

 First off, introducing Hypothesis extra packages! 

 These are packages that are separated out from core Hypothesis because they have one or more dependencies. Every hypothesis-extra package is pinned to a specific point release of Hypothesis and will have some version requirements on its dependency. They use entry_points so you will usually not need to explicitly import them, just have them installed on the path. 

 This release introduces two of them: 

 hypothesis-datetime: 

 Does what it says on the tin: Generates datetimes for Hypothesis. Just install the package and datetime support will start working. 

 Depends on pytz for timezone support 

 hypothesis-pytest: 

 A very rudimentary pytest plugin. All it does right now is hook the display of falsifying examples into pytest reporting. 

 Depends on pytest.</dl>

<h3>0.4.3 - 2015-02-05</h3>

 

 Codename: TIL narrow Python builds are a thing 

 This just fixes the one bug.
<dl>
<dt>&bull;
<dd> Apparently there is such a thing as a &quot;narrow python build&quot; and OS X ships with these by default for python 2.7. These are builds where you only have two bytes worth of unicode. As a result, generating unicode was completely broken on OS X. Fix this by only generating unicode codepoints in the range supported by the system.</dl>

<h3>0.4.2 - 2015-02-04</h3>

 

 Codename: O(dear) 

 This is purely a bugfix release:
<dl>
<dt>&bull;
<dd> Provide sensible external hashing for all core types. This will significantly improve performance of tracking seen examples which happens in literally every falsification run. For Hypothesis fixing this cut 40% off the runtime of the test suite. The behaviour is quadratic in the number of examples so if you're running the default configuration this will be less extreme (Hypothesis's test suite runs at a higher number of examples than default), but you should still see a significant improvement.
<dt>&bull;
<dd> Fix a bug in formatting of complex numbers where the string could get incorrectly truncated.</dl>

<h3>0.4.1 - 2015-02-03</h3>

 

 Codename: Cruel and unusual edge cases 

 This release is mostly about better test case generation. 

 Enhancements:
<dl>
<dt>&bull;
<dd> Has a cool release name
<dt>&bull;
<dd> text_type (str in python 3, unicode in python 2) example generation now actually produces interesting unicode instead of boring ascii strings.
<dt>&bull;
<dd> floating point numbers are generated over a much wider range, with particular attention paid to generating nasty numbers - nan, infinity, large and small values, etc.
<dt>&bull;
<dd> examples can be generated using pieces of examples previously saved in the database. This allows interesting behaviour that has previously been discovered to be propagated to other examples.
<dt>&bull;
<dd> improved parameter exploration algorithm which should allow it to more reliably hit interesting edge cases.
<dt>&bull;
<dd> Timeout can now be disabled entirely by setting it to any value &lt;= 0. 

 Bug fixes:
<dt>&bull;
<dd> The descriptor on a OneOfStrategy could be wrong if you had descriptors which were equal but should not be coalesced. e.g. a strategy for one_of((frozenset({int}), {int})) would have reported its descriptor as {int}. This is unlikely to have caused you any problems
<dt>&bull;
<dd> If you had strategies that could produce NaN (which float previously couldn't but e.g. a Just(float('nan')) could) then this would have sent hypothesis into an infinite loop that would have only been terminated when it hit the timeout.
<dt>&bull;
<dd> Given elements that can take a long time to minimize, minimization of floats or tuples could be quadratic or worse in the that value. You should now see much better performance for simplification, albeit at some cost in quality. 

 Other:
<dt>&bull;
<dd> A lot of internals have been been rewritten. This shouldn't affect you at all, but it opens the way for certain of hypothesis's oddities to be a lot more extensible by users. Whether this is a good thing may be up for debate...</dl>

<h3>0.4.0 - 2015-01-21</h3>

 

 FLAGSHIP FEATURE: Hypothesis now persists examples for later use. It stores data in a local SQLite database and will reuse it for all tests of the same type. 

 LICENSING CHANGE: Hypothesis is now released under the Mozilla Public License 2.0. This applies to all versions from 0.4.0 onwards until further notice. The previous license remains applicable to all code prior to 0.4.0. 

 Enhancements:
<dl>
<dt>&bull;
<dd> Printing of failing examples. I was finding that the pytest runner was not doing a good job of displaying these, and that Hypothesis itself could do much better.
<dt>&bull;
<dd> Drop dependency on six for cross-version compatibility. It was easy enough to write the shim for the small set of features that we care about and this lets us avoid a moderately complex dependency.
<dt>&bull;
<dd> Some improvements to statistical distribution of selecting from small (&lt;= 3 elements)
<dt>&bull;
<dd> Improvements to parameter selection for finding examples. 

 Bugs fixed:
<dt>&bull;
<dd> could_have_produced for lists, dicts and other collections would not have examined the elements and thus when using a union of different types of list this could result in Hypothesis getting confused and passing a value to the wrong strategy. This could potentially result in exceptions being thrown from within simplification.
<dt>&bull;
<dd> sampled_from would not work correctly on a single element list.
<dt>&bull;
<dd> Hypothesis could get <i>very</i> confused by values which are equal despite having different types being used in descriptors. Hypothesis now has its own more specific version of equality it uses for descriptors and tracking. It is always more fine grained than Python equality: Things considered != are not considered equal by hypothesis, but some things that are considered == are distinguished. If your test suite uses both frozenset and set tests this bug is probably affecting you.</dl>

<h3>0.3.2 - 2015-01-16</h3>

<dl>
<dt>&bull;
<dd> Fix a bug where if you specified floats_in_range with integer arguments Hypothesis would error in example simplification.
<dt>&bull;
<dd> Improve the statistical distribution of the floats you get for the floats_in_range strategy. I'm not sure whether this will affect users in practice but it took my tests for various conditions from flaky to rock solid so it at the very least improves discovery of the artificial cases I'm looking for.
<dt>&bull;
<dd> Improved repr() for strategies and RandomWithSeed instances.
<dt>&bull;
<dd> Add detection for flaky test cases where hypothesis managed to find an example which breaks it but on the final invocation of the test it does not raise an error. This will typically happen with too much recursion errors but could conceivably happen in other circumstances too.
<dt>&bull;
<dd> Provide a &quot;derandomized&quot; mode. This allows you to run hypothesis with zero real randomization, making your build nice and deterministic. The tests run with a seed calculated from the function they're testing so you should still get a good distribution of test cases.
<dt>&bull;
<dd> Add a mechanism for more conveniently defining tests which just sample from some collection.
<dt>&bull;
<dd> Fix for a really subtle bug deep in the internals of the strategy table. In some circumstances if you were to define instance strategies for both a parent class and one or more of its subclasses you would under some circumstances get the strategy for the wrong superclass of an instance. It is very unlikely anyone has ever encountered this in the wild, but it is conceivably possible given that a mix of namedtuple and tuple are used fairly extensively inside hypothesis which do exhibit this pattern of strategy.</dl>

<h3>0.3.1 - 2015-01-13</h3>

<dl>
<dt>&bull;
<dd> Support for generation of frozenset and Random values
<dt>&bull;
<dd> Correct handling of the case where a called function mutates it argument. This involved introducing a notion of a strategies knowing how to copy their argument. The default method should be entirely acceptable and the worst case is that it will continue to have the old behaviour if you don't mark your strategy as mutable, so this shouldn't break anything.
<dt>&bull;
<dd> Fix for a bug where some strategies did not correctly implement could_have_produced. It is very unlikely that any of these would have been seen in the wild, and the consequences if they had been would have been minor.
<dt>&bull;
<dd> Re-export the @given decorator from the main hypothesis namespace. It's still available at the old location too.
<dt>&bull;
<dd> Minor performance optimisation for simplifying long lists.</dl>

<h3>0.3.0 - 2015-01-12</h3>

<dl>
<dt>&bull;
<dd> Complete redesign of the data generation system. Extreme breaking change for anyone who was previously writing their own SearchStrategy implementations. These will not work any more and you'll need to modify them.
<dt>&bull;
<dd> New settings system allowing more global and modular control of Verifier behaviour.
<dt>&bull;
<dd> Decouple SearchStrategy from the StrategyTable. This leads to much more composable code which is a lot easier to understand.
<dt>&bull;
<dd> A significant amount of internal API renaming and moving. This may also break your code.
<dt>&bull;
<dd> Expanded available descriptors, allowing for generating integers or floats in a specific range.
<dt>&bull;
<dd> Significantly more robust. A very large number of small bug fixes, none of which anyone is likely to have ever noticed.
<dt>&bull;
<dd> Deprecation of support for pypy and python 3 prior to 3.3. 3.3 and 3.4. Supported versions are 2.7.x, 3.3.x, 3.4.x. I expect all of these to remain officially supported for a very long time. I would not be surprised to add pypy support back in later but I'm not going to do so until I know someone cares about it. In the meantime it will probably still work.</dl>

<h3>0.2.2 - 2015-01-08</h3>

<dl>
<dt>&bull;
<dd> Fix an embarrassing complete failure of the installer caused by my being bad at version control</dl>

<h3>0.2.1 - 2015-01-07</h3>

<dl>
<dt>&bull;
<dd> Fix a bug in the new stateful testing feature where you could make __init__ a @requires method. Simplification would not always work if the prune method was able to successfully shrink the test.</dl>

<h3>0.2.0 - 2015-01-07</h3>

<dl>
<dt>&bull;
<dd> It's aliiive.
<dt>&bull;
<dd> Improve python 3 support using six.
<dt>&bull;
<dd> Distinguish between byte and unicode types.
<dt>&bull;
<dd> Fix issues where FloatStrategy could raise.
<dt>&bull;
<dd> Allow stateful testing to request constructor args.
<dt>&bull;
<dd> Fix for issue where test annotations would timeout based on when the module was loaded instead of when the test started</dl>

<h3>0.1.4 - 2013-12-14</h3>

<dl>
<dt>&bull;
<dd> Make verification runs time bounded with a configurable timeout</dl>

<h3>0.1.3 - 2013-05-03</h3>

<dl>
<dt>&bull;
<dd> Bugfix: Stateful testing behaved incorrectly with subclassing.
<dt>&bull;
<dd> Complex number support
<dt>&bull;
<dd> support for recursive strategies
<dt>&bull;
<dd> different error for hypotheses with unsatisfiable assumptions</dl>

<h3>0.1.2 - 2013-03-24</h3>

<dl>
<dt>&bull;
<dd> Bugfix: Stateful testing was not minimizing correctly and could throw exceptions.
<dt>&bull;
<dd> Better support for recursive strategies.
<dt>&bull;
<dd> Support for named tuples.
<dt>&bull;
<dd> Much faster integer generation.</dl>

<h3>0.1.1 - 2013-03-24</h3>

<dl>
<dt>&bull;
<dd> Python 3.x support via 2to3.
<dt>&bull;
<dd> Use new style classes (oops).</dl>

<h3>0.1.0 - 2013-03-23</h3>

<dl>
<dt>&bull;
<dd> Introduce stateful testing.
<dt>&bull;
<dd> Massive rewrite of internals to add flags and strategies.</dl>

<h3>0.0.5 - 2013-03-13</h3>

<dl>
<dt>&bull;
<dd> No changes except trying to fix packaging</dl>

<h3>0.0.4 - 2013-03-13</h3>

<dl>
<dt>&bull;
<dd> No changes except that I checked in a failing test case for 0.0.3 so had to replace the release. Doh</dl>

<h3>0.0.3 - 2013-03-13</h3>

<dl>
<dt>&bull;
<dd> Improved a few internals.
<dt>&bull;
<dd> Opened up creating generators from instances as a general API.
<dt>&bull;
<dd> Test integration.</dl>

<h3>0.0.2 - 2013-03-12</h3>

<dl>
<dt>&bull;
<dd> Starting to tighten up on the internals.
<dt>&bull;
<dd> Change API to allow more flexibility in configuration.
<dt>&bull;
<dd> More testing.</dl>

<h3>0.0.1 - 2013-03-10</h3>

<dl>
<dt>&bull;
<dd> Initial release.
<dt>&bull;
<dd> Basic working prototype. Demonstrates idea, probably shouldn't be used.</dl>

<h2>ONGOING HYPOTHESIS DEVELOPMENT</h2>

 

 Hypothesis development is managed by me, <i>David R. MacIver</i>. I am the primary author of Hypothesis. 

 <i>However</i>, I no longer do unpaid feature development on Hypothesis. My roles as leader of the project are:
<dl>
<dt>1.
<dd> Helping other people do feature development on Hypothesis
<dt>2.
<dd> Fixing bugs and other code health issues
<dt>3.
<dd> Improving documentation
<dt>4.
<dd> General release management work
<dt>5.
<dd> Planning the general roadmap of the project
<dt>6.
<dd> Doing sponsored development on tasks that are too large or in depth for other people to take on 

 So all new features must either be sponsored or implemented by someone else. That being said, the maintenance team takes an active role in shepherding pull requests and helping people write a new feature (see <i>CONTRIBUTING.rst</i> for details and <i>pull request #154</i> for an example of how the process goes). This isn't &quot;patches welcome&quot;, it's &quot;we will help you write a patch&quot;.</dl>

<h3>Release Policy</h3>

 

 Hypothesis releases follow <i>semantic versioning</i>. 

 We maintain backwards-compatibility wherever possible, and use deprecation warnings to mark features that have been superseded by a newer alternative. If you want to detect this, the <b>strict setting</b> upgrades all Hypothesis warnings to errors. 

 We use continuous deployment to ensure that you can always use our newest and shiniest features - every change to the source tree is automatically built and published on PyPI as soon as it's merged onto master, after code review and passing our extensive test suite.

<h3>Project Roadmap</h3>

 

 Hypothesis does not have a long-term release plan. However some visibility into our plans for future <b>compatibility</b> may be useful:
<dl>
<dt>&bull;
<dd> We value compatibility, and maintain it as far as practical. This generally excludes things which are end-of-life upstream, or have an unstable API.
<dt>&bull;
<dd> We would like to drop Python 2 support when it it reaches end of life in 2020. Ongoing support is likely to depend on commercial funding.
<dt>&bull;
<dd> We intend to support PyPy3 as soon as it supports a recent enough version of Python 3. See <i>issue #602</i>.</dl>

<h2>HELP AND SUPPORT</h2>

 

 For questions you are happy to ask in public, the <b>Hypothesis community</b> is a friendly place where I or others will be more than happy to help you out. You're also welcome to ask questions on Stack Overflow. If you do, please tag them with 'python-hypothesis' so someone sees them. 

 For bugs and enhancements, please file an issue on the <i>GitHub issue tracker</i>. Note that as per the <b>development policy</b>, enhancements will probably not get implemented unless you're willing to pay for development or implement them yourself (with assistance from me). Bugs will tend to get fixed reasonably promptly, though it is of course on a best effort basis. 

 To see the versions of Python, optional dependencies, test runners, and operating systems Hypothesis supports (meaning incompatibility is treated as a bug), see <b>supported</b>. 

 If you need to ask questions privately or want more of a guarantee of bugs being fixed promptly, please contact me on <i>hypothesis-support [at] drmaciver.com</i> to talk about availability of support contracts.

<h2>PACKAGING GUIDELINES</h2>

 

 Downstream packagers often want to package Hypothesis. Here are some guidelines. 

 The primary guideline is this: If you are not prepared to keep up with the Hypothesis release schedule, don't. You will annoy me and are doing your users a disservice. 

 Hypothesis has quite a frequent release schedule. It's very rare that it goes a month without a release, and there are often multiple releases in a given month. 

 Many people not only fail to follow the release schedule but also seem included to package versions which are months out of date even at the point of packaging. This will cause me to be very annoyed with you and you will consequently get very little co-operation from me. 

 If you <i>are</i> prepared to keep up with the Hypothesis release schedule, the rest of this document outlines some information you might find useful.

<h3>Release tarballs</h3>

 

 These are available from <i>the GitHub releases page</i>. The tarballs on pypi are intended for installation from a Python tool such as pip and should not be considered complete releases. Requests to include additional files in them will not be granted. Their absence is not a bug.

<h3>Dependencies</h3>

<h3>Python versions</h3>

 

 Hypothesis is designed to work with a range of Python versions. Currently supported are:
<dl>
<dt>&bull;
<dd> pypy-2.6.1 (earlier versions of pypy <i>may</i> work)
<dt>&bull;
<dd> CPython 2.7.x
<dt>&bull;
<dd> CPython 3.4.x
<dt>&bull;
<dd> CPython 3.5.x
<dt>&bull;
<dd> CPython 3.6.x 

 If you feel the need to have separate Python 3 and Python 2 packages you can, but Hypothesis works unmodified on either.</dl>

<h3>Other Python libraries</h3>

 

 Hypothesis has <i>optional</i> dependencies on the following libraries:
<dl>
<dt>&bull;
<dd> pytz (almost any version should work)
<dt>&bull;
<dd> faker, version 0.7
<dt>&bull;
<dd> Django, all supported versions
<dt>&bull;
<dd> numpy, 1.10 or later (earlier versions will probably work fine)
<dt>&bull;
<dd> py.test (2.7.0 or greater). This is a mandatory dependency for testing Hypothesis itself but optional for users. 

 The way this works when installing Hypothesis normally is that these features become available if the relevant library is installed.</dl>

<h3>Testing Hypothesis</h3>

 

 If you want to test Hypothesis as part of your packaging you will probably not want to use the mechanisms Hypothesis itself uses for running its tests, because it has a lot of logic for installing and testing against different versions of Python. 

 The tests must be run with py.test. A version more recent than 2.7.0 is strongly encouraged, but it may work with earlier versions (however py.test specific logic is disabled before 2.7.0). 

 Tests are organised into a number of top level subdirectories of the tests/ directory.
<dl>
<dt>&bull;
<dd> cover: This is a small, reasonably fast, collection of tests designed to give 100% coverage of all but a select subset of the files when run under Python 3.
<dt>&bull;
<dd> nocover: This is a much slower collection of tests that should not be run under coverage for performance reasons.
<dt>&bull;
<dd> py2: Tests that can only be run under Python 2
<dt>&bull;
<dd> py3: Tests that can only be run under Python 3
<dt>&bull;
<dd> datetime: This tests the subset of Hypothesis that depends on pytz
<dt>&bull;
<dd> fakefactory: This tests the subset of Hypothesis that depends on fakefactory.
<dt>&bull;
<dd> django: This tests the subset of Hypothesis that depends on django (this also depends on fakefactory). 

 An example invocation for running the coverage subset of these tests: 

 <pre>
pip install -e .
pip install pytest # you will probably want to use your own packaging here
python -m pytest tests/cover
</pre></dl>

<h3>Examples</h3>

<dl>
<dt>&bull;
<dd> <i>arch linux</i>
<dt>&bull;
<dd> <i>fedora</i>
<dt>&bull;
<dd> <i>gentoo</i> (slightly behind at the time of this writing)</dl>

<h2>AUTHOR</h2>

 David R. MacIver

<h2>COPYRIGHT</h2>

 2013-2017, David R. MacIver 

<h2>Index</h2>



<dt><a HREF="#lbAI">DETAILS AND ADVANCED FEATURES</a>
<dd>


<dt><a HREF="#lbAS">SETTINGS</a>
<dd>


<dt><a HREF="#lbAY">WHAT YOU CAN GENERATE AND HOW</a>
<dd>


<dt><a HREF="#lbBI">ADDITIONAL PACKAGES</a>
<dd>


<dt><a HREF="#lbBO">HYPOTHESIS FOR DJANGO USERS</a>
<dd>


<dt><a HREF="#lbBT">SCIENTIFIC HYPOTHESIS (FOR NUMPY)</a>
<dd>
<dt><a HREF="#lbBU">HEALTH CHECKS</a>
<dd>
<dt><a HREF="#lbBV">THE HYPOTHESIS EXAMPLE DATABASE</a>
<dd>


<dt><a HREF="#lbCA">STATEFUL TESTING</a>
<dd>


<dt><a HREF="#lbCG">COMPATIBILITY</a>
<dd>


<dt><a HREF="#lbCN">SOME MORE EXAMPLES</a>
<dd>


<dt><a HREF="#lbCS">COMMUNITY</a>
<dd>


<dt><a HREF="#lbCV">THE PURPOSE OF HYPOTHESIS</a>
<dd>
<dt><a HREF="#lbCW">TESTIMONIALS</a>
<dd>


<dt><a HREF="#lbDJ">OPEN SOURCE PROJECTS USING HYPOTHESIS</a>
<dd>
<dt><a HREF="#lbDK">PROJECTS EXTENDING HYPOTHESIS</a>
<dd>
<dt><a HREF="#lbDL">CHANGELOG</a>
<dd>


<dt><a HREF="#lbHV">ONGOING HYPOTHESIS DEVELOPMENT</a>
<dd>


<dt><a HREF="#lbHY">HELP AND SUPPORT</a>
<dd>
<dt><a HREF="#lbHZ">PACKAGING GUIDELINES</a>
<dd>


<dt><a HREF="#lbIG">AUTHOR</a>
<dd>
<dt><a HREF="#lbIH">COPYRIGHT</a>
<dd></dl>
