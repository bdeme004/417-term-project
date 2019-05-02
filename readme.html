<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1" />
<meta name="generator" content="pdoc 0.5.4" />
<title>approximations API documentation</title>
<meta name="description" content="" />
<link href='https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.0/normalize.min.css' rel='stylesheet'>
<link href='https://cdnjs.cloudflare.com/ajax/libs/10up-sanitize.css/8.0.0/sanitize.min.css' rel='stylesheet'>
<link href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.12.0/styles/github.min.css" rel="stylesheet">
<style>.flex{display:flex !important}body{line-height:1.5em}#content{padding:20px}#sidebar{padding:30px;overflow:hidden}.http-server-breadcrumbs{font-size:130%;margin:0 0 15px 0}#footer{font-size:.75em;padding:5px 30px;border-top:1px solid #ddd;text-align:right}#footer p{margin:0 0 0 1em;display:inline-block}#footer p:last-child{margin-right:30px}h1,h2,h3,h4,h5{font-weight:300}h1{font-size:2.5em;line-height:1.1em}h2{font-size:1.75em;margin:1em 0 .50em 0}h3{font-size:1.4em;margin:25px 0 10px 0}h4{margin:0;font-size:105%}a{color:#058;text-decoration:none;transition:color .3s ease-in-out}a:hover{color:#e82}.title code{font-weight:bold}h2[id^="header-"]{margin-top:2em}.ident{color:#900}pre code{background:#f8f8f8;font-size:.8em;line-height:1.4em}code{background:#f2f2f1;padding:1px 4px;overflow-wrap:break-word}h1 code{background:transparent}pre{background:#f8f8f8;border:0;border-top:1px solid #ccc;border-bottom:1px solid #ccc;margin:1em 0;padding:1ex}#http-server-module-list{display:flex;flex-flow:column}#http-server-module-list div{display:flex}#http-server-module-list dt{min-width:10%}#http-server-module-list p{margin-top:0}.toc ul,#index{list-style-type:none;margin:0;padding:0}#index code{background:transparent}#index h3{border-bottom:1px solid #ddd}#index ul{padding:0}#index h4{font-weight:bold}#index h4 + ul{margin-bottom:.6em}@media (min-width:200ex){#index .two-column{column-count:2}}@media (min-width:300ex){#index .two-column{column-count:3}}dl{margin-bottom:2em}dl dl:last-child{margin-bottom:4em}dd{margin:0 0 1em 3em}#header-classes + dl > dd{margin-bottom:3em}dd dd{margin-left:2em}dd p{margin:10px 0}.name{background:#eee;font-weight:bold;font-size:.85em;padding:5px 10px;display:inline-block;min-width:40%}.name:hover{background:#e0e0e0}.name > span:first-child{white-space:nowrap}.name.class > span:nth-child(2){margin-left:.4em}.name small{font-weight:normal}.inherited{color:#999;border-left:5px solid #eee;padding-left:1em}.inheritance em{font-style:normal;font-weight:bold}.desc h2{font-weight:400;font-size:1.25em}.desc h3{font-size:1em}.desc dt code{background:inherit}.source summary{color:#666;text-align:right;font-weight:400;font-size:.8em;text-transform:uppercase;cursor:pointer}.source pre{max-height:500px;overflow:auto;margin:0}.source pre code{font-size:12px;overflow:visible}.hlist{list-style:none}.hlist li{display:inline}.hlist li:after{content:',\2002'}.hlist li:last-child:after{content:none}.hlist .hlist{display:inline;padding-left:1em}img{max-width:100%}.admonition{padding:.1em .5em}.admonition-title{font-weight:bold}.admonition.note,.admonition.info,.admonition.important{background:#aef}.admonition.todo,.admonition.versionadded,.admonition.tip,.admonition.hint{background:#dfd}.admonition.warning,.admonition.versionchanged,.admonition.deprecated{background:#fd4}.admonition.error,.admonition.danger,.admonition.caution{background:lightpink}</style>
<style media="screen and (min-width: 700px)">@media screen and (min-width:700px){#sidebar{width:30%}#content{width:70%;max-width:100ch;padding:3em 4em;border-left:1px solid #ddd}pre code{font-size:1em}.item .name{font-size:1em}main{display:flex;flex-direction:row-reverse;justify-content:flex-end}.toc ul ul,#index ul{padding-left:1.5em}.toc > ul > li{margin-top:.5em}}</style>
<style media="print">@media print{#sidebar h1{page-break-before:always}.source{display:none}}@media print{*{background:transparent !important;color:#000 !important;box-shadow:none !important;text-shadow:none !important}a[href]:after{content:" (" attr(href) ")";font-size:90%}a[href][title]:after{content:none}abbr[title]:after{content:" (" attr(title) ")"}.ir a:after,a[href^="javascript:"]:after,a[href^="#"]:after{content:""}pre,blockquote{border:1px solid #999;page-break-inside:avoid}thead{display:table-header-group}tr,img{page-break-inside:avoid}img{max-width:100% !important}@page{margin:0.5cm}p,h2,h3{orphans:3;widows:3}h1,h2,h3,h4,h5,h6{page-break-after:avoid}}</style>
</head>
<body>
<main>
<article id="content">
<header>
<h1 class="title"><code>approximations</code> module</h1>
</header>
<section id="section-intro">
<details class="source">
<summary>Source code</summary>
<pre><code class="python">import numpy as np
from numpy.polynomial import Polynomial as npp
import re


def load_data(infile):
    &#34;&#34;&#34;Return a list of dictionaries, each containing data for one core.&#34;&#34;&#34;
    with open(infile) as inf:
        cores = [dict(), dict(), dict(), dict()]
        time = 0
        for line in inf:
            temps = [make_float(val) for val in line.split()]
            for val in temps:
                i = temps.index(val)
                cores[i].setdefault(time, val)
            time += 30
    return cores


def make_float(string):
    &#34;&#34;&#34;Convert a given string representation into a floating point number.

    The string is assumed to be any number of digits before and after a decimal
    point, optionally preceded by + or -.
    &#34;&#34;&#34;
    pattern = re.compile(&#34;[+-]*\\d+(\\.\\d+)*&#34;)
    result = pattern.match(string)
    if(result):
        return float(result.group())
    return None


def print_data(data):
    &#34;&#34;&#34;Print the input data in a table.&#34;&#34;&#34;
    print(&#34;time(sec)\ttemperature (C)&#34;)
    print(&#34;\t\tC1\t  C2\t    C3\t      C4&#34;)
    for x in data[0].keys():
        print(&#34;%d\t\t%f %f %f %f&#34;
              % (x, data[0][x], data[1][x], data[2][x], data[3][x]))


class leastSquares:
    &#34;&#34;&#34;Global least-squares approximation of the input data.&#34;&#34;&#34;

    def __init__(self, dataset, n=2):
        &#34;&#34;&#34;Determine an approximating linear function using n basis functions.

        Values of n other than 2 are not currently supported. Arguments passed
        to the n parameter are ignored.
        &#34;&#34;&#34;
        n = 2
        x = [x for x in dataset]
        y = [dataset[x] for x in dataset]

        A = np.array([self.make_row(i, x) for i in range(0, n)])
        b = np.array([self.make_row_b(i, x, y) for i in range(0, n)])

        c = np.linalg.lstsq(A, b, rcond=None)
        self.x = x
        self.coef = c[0]

    def basis_PI(self, n, x):
        &#34;&#34;&#34;Return the value of the nth basis function at x.&#34;&#34;&#34;
        if n == 0:
            return 1
        return x

    def sum_PIiPIj(self, i, j, x):
        &#34;&#34;&#34;Return an integer equal to the sum of all (PIi(x) * PIj(x))
        where PIi is the ith basis function and PIj is the jth basis function.&#34;&#34;&#34;
        k = len(x)
        PIiPIj = [self.basis_PI(i, x[r]) * self.basis_PI(j, x[r]) for r in range(0, k)]
        return sum(PIiPIj)

    def make_row(self, i, x):
        &#34;&#34;&#34;Return an array which represents one row of a matrix A.&#34;&#34;&#34;
        return [self.sum_PIiPIj(i, j, x) for j in range(0, 2)]

    def make_row_b(self, i, x, y):
        &#34;&#34;&#34;Return an array which represents one row of a vector b.&#34;&#34;&#34;
        k = len(x)
        PIiY = [self.basis_PI(i, x[r]) * y[r] for r in range(0, k)]
        return [sum(PIiY)]

    def toString(self):
        &#34;&#34;&#34;Return a string representation of the approximation polynomial.&#34;&#34;&#34;
        return (&#34;%d &lt;= x &lt; %d; y = %.3f + %.3fx; least-squares\n&#34;
                % (self.x[0], self.x[-1], self.coef[0], self.coef[1])
                )


class linear:
    &#34;&#34;&#34;Set of piecewise linear interpolation functions of the input data.&#34;&#34;&#34;
    def __init__(self, dataset):
        &#34;&#34;&#34;Determine a linear interpolation between point i and i+1 for all i.
        &#34;&#34;&#34;
        self.coef = []
        self.x = list(dataset.keys())

        x0, y0 = (None, None)
        x1, y1 = (None, None)

        for (x, y) in dataset.items():
            if x0 is None:
                x0, y0 = (x, y)
                continue
            x1, y1 = (x, y)
            c0 = y0 / (x0 - x1)
            c1 = y1 / (x1 - x0)
            px = npp([(-c0 * x1), c0]) + npp([(-c1 * x0), c1])
            px.coef.resize((1, 2))
            self.coef.append(px.coef[0])
            x0, y0 = (x, y)

    def toList(self):
        &#34;&#34;&#34;Return a list containing one string representation per linear interpolant.&#34;&#34;&#34;
        i = 0
        li = []
        for c in self.coef:
            li.append(&#34;%d &lt;= x &lt; %d; y%d = %.3f + %.fx; linear interpolation&#34;
                      % (self.x[i], self.x[i + 1], i, c[0], c[1])
                      )
            i += 1
        return li

    def toString(self):
        &#34;&#34;&#34;Return a single string representation of all linear interpolants.

        **print(lsq.toString())** produces the same visual output as
        **for line in lsq.toList(): print(line)**.
        &#34;&#34;&#34;
        i = 0
        s = &#34;&#34;
        for c in self.coef:
            s += (&#34;%d &lt;= x &lt; %d; y%d = %.3f + %.3fx; linear interpolation\n&#34;
                  % (self.x[i], self.x[i + 1],
                     i, c[0], c[1])
                  )
            i += 1
        return s


class cubicSpline:
    &#34;&#34;&#34;Set of piecewise cubic interpolation functions of the input data.&#34;&#34;&#34;
    def __init__(self, dataset):
        &#34;&#34;&#34;Determine a linear interpolation between point i and i+1 for all i.
        &#34;&#34;&#34;
        result = dict()
        p0 = p1 = p2 = None
        i = 0

        for (x, y) in dataset.items():
            if p0 is None:
                p0 = (x, y)
                continue
            if p1 is None:
                p1 = (x, y)
                continue
            p2 = (x, y)
            s0, s1 = self.solve_matrix(p0, p1, p2)
            result.setdefault(i, s0)
            i += 1
            result.setdefault(i, s1)
            p0 = p1
            p1 = p2

            self.coef = list(result.values())
            self.x = list(dataset.keys())

    def solve_matrix(self, p0, p1, p2):
        &#34;&#34;&#34;Return a tuple of two arrays, each containing the coefficients
        to a cubic interpolant.
        &#34;&#34;&#34;
        x0, y0 = p0
        x1, y1 = p1
        x2, y2 = p2

        A = np.array((
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [1, (x1 - x0), ((x1 - x0) ** 2), ((x1 - x0) ** 3), 0, 0, 0, 0],
            [0, 0, 0, 0, 1, (x2 - x1), ((x2 - x1) ** 2), ((x2 - x1) ** 3)],
            [0, 1, (2 * (x1 - x0)), (3 * ((x1 - x0) ** 2)), 0, -1, 0, 0],
            [0, 0, 2, (6 * ((x1 - x0) ** 2)), 0, 0, -2, 0],
            [0, 0, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 2, (6 * ((x2 - x1) ** 2))]
        ))

        b = np.array((
            [y0],
            [y1],
            [y1],
            [y2],
            [0],
            [0],
            [0],
            [0]
        ))

        c = np.linalg.lstsq(A, b, rcond=None)
        c0 = c[0][0:4]
        c1 = c[0][4:8]

        return (c0, c1)

    def toList(self):
        &#34;&#34;&#34;Return a list containing one string representation per linear interpolant.&#34;&#34;&#34;
        i = 0
        li = []
        for c in self.coef:
            # broken up into substrings because it&#39;s really long.
            s = &#34;&#34;
            s += &#34;%d &lt;= x &lt; %d;&#34; % (self.x[i], self.x[i + 1])
            s += &#34;y%d = %.3f + %.3f(x-%d)&#34; % (i, c[0], c[1], self.x[i])
            s += &#34; + %.3f(x-%d)^2&#34; % (c[2], self.x[i])
            s += &#34; + %.3f(x-%d)^3&#34; % (c[3], self.x[i])
            s += &#34;; cubic spline interpolation&#34;

            li.append(s)
            i += 1
        return li

    def toString(self):
        &#34;&#34;&#34;Return a single string representation of all linear interpolants.

        **print(csp.toString())** produces the same visual output as
        **for line in csp.toList(): print(line)**.
        &#34;&#34;&#34;
        i = 0
        s = &#34;&#34;
        for c in self.coef:
            # broken up into substrings because it&#39;s really long.
            s += &#34;%d &lt;= x &lt; %d; &#34; % (self.x[i], self.x[i + 1])
            s += &#34;y%d = %.3f + %.3f(x-%d)&#34; % (i, c[0], c[1], self.x[i])
            s += &#34; + %.3f(x-%d)^2&#34; % (c[2], self.x[i])
            s += &#34; + %.3f(x-%d)^3&#34; % (c[3], self.x[i])
            s += &#34;; cubic spline interpolation&#34;
            s += &#34;\n&#34;
            i += 1
        return s</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="approximations.load_data"><code class="name flex">
<span>def <span class="ident">load_data</span></span>(<span>infile)</span>
</code></dt>
<dd>
<section class="desc"><p>Return a list of dictionaries, each containing data for one core.</p></section>
<details class="source">
<summary>Source code</summary>
<pre><code class="python">def load_data(infile):
    &#34;&#34;&#34;Return a list of dictionaries, each containing data for one core.&#34;&#34;&#34;
    with open(infile) as inf:
        cores = [dict(), dict(), dict(), dict()]
        time = 0
        for line in inf:
            temps = [make_float(val) for val in line.split()]
            for val in temps:
                i = temps.index(val)
                cores[i].setdefault(time, val)
            time += 30
    return cores</code></pre>
</details>
</dd>
<dt id="approximations.make_float"><code class="name flex">
<span>def <span class="ident">make_float</span></span>(<span>string)</span>
</code></dt>
<dd>
<section class="desc"><p>Convert a given string representation into a floating point number.</p>
<p>The string is assumed to be any number of digits before and after a decimal
point, optionally preceded by + or -.</p></section>
<details class="source">
<summary>Source code</summary>
<pre><code class="python">def make_float(string):
    &#34;&#34;&#34;Convert a given string representation into a floating point number.

    The string is assumed to be any number of digits before and after a decimal
    point, optionally preceded by + or -.
    &#34;&#34;&#34;
    pattern = re.compile(&#34;[+-]*\\d+(\\.\\d+)*&#34;)
    result = pattern.match(string)
    if(result):
        return float(result.group())
    return None</code></pre>
</details>
</dd>
<dt id="approximations.print_data"><code class="name flex">
<span>def <span class="ident">print_data</span></span>(<span>data)</span>
</code></dt>
<dd>
<section class="desc"><p>Print the input data in a table.</p></section>
<details class="source">
<summary>Source code</summary>
<pre><code class="python">def print_data(data):
    &#34;&#34;&#34;Print the input data in a table.&#34;&#34;&#34;
    print(&#34;time(sec)\ttemperature (C)&#34;)
    print(&#34;\t\tC1\t  C2\t    C3\t      C4&#34;)
    for x in data[0].keys():
        print(&#34;%d\t\t%f %f %f %f&#34;
              % (x, data[0][x], data[1][x], data[2][x], data[3][x]))</code></pre>
</details>
</dd>
</dl>
</section>
<section>
<h2 class="section-title" id="header-classes">Classes</h2>
<dl>
<dt id="approximations.cubicSpline"><code class="flex name class">
<span>class <span class="ident">cubicSpline</span></span>
</code></dt>
<dd>
<section class="desc"><p>Set of piecewise cubic interpolation functions of the input data.</p></section>
<details class="source">
<summary>Source code</summary>
<pre><code class="python">class cubicSpline:
    &#34;&#34;&#34;Set of piecewise cubic interpolation functions of the input data.&#34;&#34;&#34;
    def __init__(self, dataset):
        &#34;&#34;&#34;Determine a linear interpolation between point i and i+1 for all i.
        &#34;&#34;&#34;
        result = dict()
        p0 = p1 = p2 = None
        i = 0

        for (x, y) in dataset.items():
            if p0 is None:
                p0 = (x, y)
                continue
            if p1 is None:
                p1 = (x, y)
                continue
            p2 = (x, y)
            s0, s1 = self.solve_matrix(p0, p1, p2)
            result.setdefault(i, s0)
            i += 1
            result.setdefault(i, s1)
            p0 = p1
            p1 = p2

            self.coef = list(result.values())
            self.x = list(dataset.keys())

    def solve_matrix(self, p0, p1, p2):
        &#34;&#34;&#34;Return a tuple of two arrays, each containing the coefficients
        to a cubic interpolant.
        &#34;&#34;&#34;
        x0, y0 = p0
        x1, y1 = p1
        x2, y2 = p2

        A = np.array((
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [1, (x1 - x0), ((x1 - x0) ** 2), ((x1 - x0) ** 3), 0, 0, 0, 0],
            [0, 0, 0, 0, 1, (x2 - x1), ((x2 - x1) ** 2), ((x2 - x1) ** 3)],
            [0, 1, (2 * (x1 - x0)), (3 * ((x1 - x0) ** 2)), 0, -1, 0, 0],
            [0, 0, 2, (6 * ((x1 - x0) ** 2)), 0, 0, -2, 0],
            [0, 0, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 2, (6 * ((x2 - x1) ** 2))]
        ))

        b = np.array((
            [y0],
            [y1],
            [y1],
            [y2],
            [0],
            [0],
            [0],
            [0]
        ))

        c = np.linalg.lstsq(A, b, rcond=None)
        c0 = c[0][0:4]
        c1 = c[0][4:8]

        return (c0, c1)

    def toList(self):
        &#34;&#34;&#34;Return a list containing one string representation per linear interpolant.&#34;&#34;&#34;
        i = 0
        li = []
        for c in self.coef:
            # broken up into substrings because it&#39;s really long.
            s = &#34;&#34;
            s += &#34;%d &lt;= x &lt; %d;&#34; % (self.x[i], self.x[i + 1])
            s += &#34;y%d = %.3f + %.3f(x-%d)&#34; % (i, c[0], c[1], self.x[i])
            s += &#34; + %.3f(x-%d)^2&#34; % (c[2], self.x[i])
            s += &#34; + %.3f(x-%d)^3&#34; % (c[3], self.x[i])
            s += &#34;; cubic spline interpolation&#34;

            li.append(s)
            i += 1
        return li

    def toString(self):
        &#34;&#34;&#34;Return a single string representation of all linear interpolants.

        **print(csp.toString())** produces the same visual output as
        **for line in csp.toList(): print(line)**.
        &#34;&#34;&#34;
        i = 0
        s = &#34;&#34;
        for c in self.coef:
            # broken up into substrings because it&#39;s really long.
            s += &#34;%d &lt;= x &lt; %d; &#34; % (self.x[i], self.x[i + 1])
            s += &#34;y%d = %.3f + %.3f(x-%d)&#34; % (i, c[0], c[1], self.x[i])
            s += &#34; + %.3f(x-%d)^2&#34; % (c[2], self.x[i])
            s += &#34; + %.3f(x-%d)^3&#34; % (c[3], self.x[i])
            s += &#34;; cubic spline interpolation&#34;
            s += &#34;\n&#34;
            i += 1
        return s</code></pre>
</details>
<h3>Methods</h3>
<dl>
<dt id="approximations.cubicSpline.__init__"><code class="name flex">
<span>def <span class="ident">__init__</span></span>(<span>self, dataset)</span>
</code></dt>
<dd>
<section class="desc"><p>Determine a linear interpolation between point i and i+1 for all i.</p></section>
<details class="source">
<summary>Source code</summary>
<pre><code class="python">def __init__(self, dataset):
    &#34;&#34;&#34;Determine a linear interpolation between point i and i+1 for all i.
    &#34;&#34;&#34;
    result = dict()
    p0 = p1 = p2 = None
    i = 0

    for (x, y) in dataset.items():
        if p0 is None:
            p0 = (x, y)
            continue
        if p1 is None:
            p1 = (x, y)
            continue
        p2 = (x, y)
        s0, s1 = self.solve_matrix(p0, p1, p2)
        result.setdefault(i, s0)
        i += 1
        result.setdefault(i, s1)
        p0 = p1
        p1 = p2

        self.coef = list(result.values())
        self.x = list(dataset.keys())</code></pre>
</details>
</dd>
<dt id="approximations.cubicSpline.solve_matrix"><code class="name flex">
<span>def <span class="ident">solve_matrix</span></span>(<span>self, p0, p1, p2)</span>
</code></dt>
<dd>
<section class="desc"><p>Return a tuple of two arrays, each containing the coefficients
to a cubic interpolant.</p></section>
<details class="source">
<summary>Source code</summary>
<pre><code class="python">def solve_matrix(self, p0, p1, p2):
    &#34;&#34;&#34;Return a tuple of two arrays, each containing the coefficients
    to a cubic interpolant.
    &#34;&#34;&#34;
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2

    A = np.array((
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [1, (x1 - x0), ((x1 - x0) ** 2), ((x1 - x0) ** 3), 0, 0, 0, 0],
        [0, 0, 0, 0, 1, (x2 - x1), ((x2 - x1) ** 2), ((x2 - x1) ** 3)],
        [0, 1, (2 * (x1 - x0)), (3 * ((x1 - x0) ** 2)), 0, -1, 0, 0],
        [0, 0, 2, (6 * ((x1 - x0) ** 2)), 0, 0, -2, 0],
        [0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, (6 * ((x2 - x1) ** 2))]
    ))

    b = np.array((
        [y0],
        [y1],
        [y1],
        [y2],
        [0],
        [0],
        [0],
        [0]
    ))

    c = np.linalg.lstsq(A, b, rcond=None)
    c0 = c[0][0:4]
    c1 = c[0][4:8]

    return (c0, c1)</code></pre>
</details>
</dd>
<dt id="approximations.cubicSpline.toList"><code class="name flex">
<span>def <span class="ident">toList</span></span>(<span>self)</span>
</code></dt>
<dd>
<section class="desc"><p>Return a list containing one string representation per linear interpolant.</p></section>
<details class="source">
<summary>Source code</summary>
<pre><code class="python">def toList(self):
    &#34;&#34;&#34;Return a list containing one string representation per linear interpolant.&#34;&#34;&#34;
    i = 0
    li = []
    for c in self.coef:
        # broken up into substrings because it&#39;s really long.
        s = &#34;&#34;
        s += &#34;%d &lt;= x &lt; %d;&#34; % (self.x[i], self.x[i + 1])
        s += &#34;y%d = %.3f + %.3f(x-%d)&#34; % (i, c[0], c[1], self.x[i])
        s += &#34; + %.3f(x-%d)^2&#34; % (c[2], self.x[i])
        s += &#34; + %.3f(x-%d)^3&#34; % (c[3], self.x[i])
        s += &#34;; cubic spline interpolation&#34;

        li.append(s)
        i += 1
    return li</code></pre>
</details>
</dd>
<dt id="approximations.cubicSpline.toString"><code class="name flex">
<span>def <span class="ident">toString</span></span>(<span>self)</span>
</code></dt>
<dd>
<section class="desc"><p>Return a single string representation of all linear interpolants.</p>
<p><strong>print(csp.toString())</strong> produces the same visual output as
<strong>for line in csp.toList(): print(line)</strong>.</p></section>
<details class="source">
<summary>Source code</summary>
<pre><code class="python">def toString(self):
    &#34;&#34;&#34;Return a single string representation of all linear interpolants.

    **print(csp.toString())** produces the same visual output as
    **for line in csp.toList(): print(line)**.
    &#34;&#34;&#34;
    i = 0
    s = &#34;&#34;
    for c in self.coef:
        # broken up into substrings because it&#39;s really long.
        s += &#34;%d &lt;= x &lt; %d; &#34; % (self.x[i], self.x[i + 1])
        s += &#34;y%d = %.3f + %.3f(x-%d)&#34; % (i, c[0], c[1], self.x[i])
        s += &#34; + %.3f(x-%d)^2&#34; % (c[2], self.x[i])
        s += &#34; + %.3f(x-%d)^3&#34; % (c[3], self.x[i])
        s += &#34;; cubic spline interpolation&#34;
        s += &#34;\n&#34;
        i += 1
    return s</code></pre>
</details>
</dd>
</dl>
</dd>
<dt id="approximations.leastSquares"><code class="flex name class">
<span>class <span class="ident">leastSquares</span></span>
</code></dt>
<dd>
<section class="desc"><p>Global least-squares approximation of the input data.</p></section>
<details class="source">
<summary>Source code</summary>
<pre><code class="python">class leastSquares:
    &#34;&#34;&#34;Global least-squares approximation of the input data.&#34;&#34;&#34;

    def __init__(self, dataset, n=2):
        &#34;&#34;&#34;Determine an approximating linear function using n basis functions.

        Values of n other than 2 are not currently supported. Arguments passed
        to the n parameter are ignored.
        &#34;&#34;&#34;
        n = 2
        x = [x for x in dataset]
        y = [dataset[x] for x in dataset]

        A = np.array([self.make_row(i, x) for i in range(0, n)])
        b = np.array([self.make_row_b(i, x, y) for i in range(0, n)])

        c = np.linalg.lstsq(A, b, rcond=None)
        self.x = x
        self.coef = c[0]

    def basis_PI(self, n, x):
        &#34;&#34;&#34;Return the value of the nth basis function at x.&#34;&#34;&#34;
        if n == 0:
            return 1
        return x

    def sum_PIiPIj(self, i, j, x):
        &#34;&#34;&#34;Return an integer equal to the sum of all (PIi(x) * PIj(x))
        where PIi is the ith basis function and PIj is the jth basis function.&#34;&#34;&#34;
        k = len(x)
        PIiPIj = [self.basis_PI(i, x[r]) * self.basis_PI(j, x[r]) for r in range(0, k)]
        return sum(PIiPIj)

    def make_row(self, i, x):
        &#34;&#34;&#34;Return an array which represents one row of a matrix A.&#34;&#34;&#34;
        return [self.sum_PIiPIj(i, j, x) for j in range(0, 2)]

    def make_row_b(self, i, x, y):
        &#34;&#34;&#34;Return an array which represents one row of a vector b.&#34;&#34;&#34;
        k = len(x)
        PIiY = [self.basis_PI(i, x[r]) * y[r] for r in range(0, k)]
        return [sum(PIiY)]

    def toString(self):
        &#34;&#34;&#34;Return a string representation of the approximation polynomial.&#34;&#34;&#34;
        return (&#34;%d &lt;= x &lt; %d; y = %.3f + %.3fx; least-squares\n&#34;
                % (self.x[0], self.x[-1], self.coef[0], self.coef[1])
                )</code></pre>
</details>
<h3>Methods</h3>
<dl>
<dt id="approximations.leastSquares.__init__"><code class="name flex">
<span>def <span class="ident">__init__</span></span>(<span>self, dataset, n=2)</span>
</code></dt>
<dd>
<section class="desc"><p>Determine an approximating linear function using n basis functions.</p>
<p>Values of n other than 2 are not currently supported. Arguments passed
to the n parameter are ignored.</p></section>
<details class="source">
<summary>Source code</summary>
<pre><code class="python">def __init__(self, dataset, n=2):
    &#34;&#34;&#34;Determine an approximating linear function using n basis functions.

    Values of n other than 2 are not currently supported. Arguments passed
    to the n parameter are ignored.
    &#34;&#34;&#34;
    n = 2
    x = [x for x in dataset]
    y = [dataset[x] for x in dataset]

    A = np.array([self.make_row(i, x) for i in range(0, n)])
    b = np.array([self.make_row_b(i, x, y) for i in range(0, n)])

    c = np.linalg.lstsq(A, b, rcond=None)
    self.x = x
    self.coef = c[0]</code></pre>
</details>
</dd>
<dt id="approximations.leastSquares.basis_PI"><code class="name flex">
<span>def <span class="ident">basis_PI</span></span>(<span>self, n, x)</span>
</code></dt>
<dd>
<section class="desc"><p>Return the value of the nth basis function at x.</p></section>
<details class="source">
<summary>Source code</summary>
<pre><code class="python">def basis_PI(self, n, x):
    &#34;&#34;&#34;Return the value of the nth basis function at x.&#34;&#34;&#34;
    if n == 0:
        return 1
    return x</code></pre>
</details>
</dd>
<dt id="approximations.leastSquares.make_row"><code class="name flex">
<span>def <span class="ident">make_row</span></span>(<span>self, i, x)</span>
</code></dt>
<dd>
<section class="desc"><p>Return an array which represents one row of a matrix A.</p></section>
<details class="source">
<summary>Source code</summary>
<pre><code class="python">def make_row(self, i, x):
    &#34;&#34;&#34;Return an array which represents one row of a matrix A.&#34;&#34;&#34;
    return [self.sum_PIiPIj(i, j, x) for j in range(0, 2)]</code></pre>
</details>
</dd>
<dt id="approximations.leastSquares.make_row_b"><code class="name flex">
<span>def <span class="ident">make_row_b</span></span>(<span>self, i, x, y)</span>
</code></dt>
<dd>
<section class="desc"><p>Return an array which represents one row of a vector b.</p></section>
<details class="source">
<summary>Source code</summary>
<pre><code class="python">def make_row_b(self, i, x, y):
    &#34;&#34;&#34;Return an array which represents one row of a vector b.&#34;&#34;&#34;
    k = len(x)
    PIiY = [self.basis_PI(i, x[r]) * y[r] for r in range(0, k)]
    return [sum(PIiY)]</code></pre>
</details>
</dd>
<dt id="approximations.leastSquares.sum_PIiPIj"><code class="name flex">
<span>def <span class="ident">sum_PIiPIj</span></span>(<span>self, i, j, x)</span>
</code></dt>
<dd>
<section class="desc"><p>Return an integer equal to the sum of all (PIi(x) * PIj(x))
where PIi is the ith basis function and PIj is the jth basis function.</p></section>
<details class="source">
<summary>Source code</summary>
<pre><code class="python">def sum_PIiPIj(self, i, j, x):
    &#34;&#34;&#34;Return an integer equal to the sum of all (PIi(x) * PIj(x))
    where PIi is the ith basis function and PIj is the jth basis function.&#34;&#34;&#34;
    k = len(x)
    PIiPIj = [self.basis_PI(i, x[r]) * self.basis_PI(j, x[r]) for r in range(0, k)]
    return sum(PIiPIj)</code></pre>
</details>
</dd>
<dt id="approximations.leastSquares.toString"><code class="name flex">
<span>def <span class="ident">toString</span></span>(<span>self)</span>
</code></dt>
<dd>
<section class="desc"><p>Return a string representation of the approximation polynomial.</p></section>
<details class="source">
<summary>Source code</summary>
<pre><code class="python">def toString(self):
    &#34;&#34;&#34;Return a string representation of the approximation polynomial.&#34;&#34;&#34;
    return (&#34;%d &lt;= x &lt; %d; y = %.3f + %.3fx; least-squares\n&#34;
            % (self.x[0], self.x[-1], self.coef[0], self.coef[1])
            )</code></pre>
</details>
</dd>
</dl>
</dd>
<dt id="approximations.linear"><code class="flex name class">
<span>class <span class="ident">linear</span></span>
</code></dt>
<dd>
<section class="desc"><p>Set of piecewise linear interpolation functions of the input data.</p></section>
<details class="source">
<summary>Source code</summary>
<pre><code class="python">class linear:
    &#34;&#34;&#34;Set of piecewise linear interpolation functions of the input data.&#34;&#34;&#34;
    def __init__(self, dataset):
        &#34;&#34;&#34;Determine a linear interpolation between point i and i+1 for all i.
        &#34;&#34;&#34;
        self.coef = []
        self.x = list(dataset.keys())

        x0, y0 = (None, None)
        x1, y1 = (None, None)

        for (x, y) in dataset.items():
            if x0 is None:
                x0, y0 = (x, y)
                continue
            x1, y1 = (x, y)
            c0 = y0 / (x0 - x1)
            c1 = y1 / (x1 - x0)
            px = npp([(-c0 * x1), c0]) + npp([(-c1 * x0), c1])
            px.coef.resize((1, 2))
            self.coef.append(px.coef[0])
            x0, y0 = (x, y)

    def toList(self):
        &#34;&#34;&#34;Return a list containing one string representation per linear interpolant.&#34;&#34;&#34;
        i = 0
        li = []
        for c in self.coef:
            li.append(&#34;%d &lt;= x &lt; %d; y%d = %.3f + %.fx; linear interpolation&#34;
                      % (self.x[i], self.x[i + 1], i, c[0], c[1])
                      )
            i += 1
        return li

    def toString(self):
        &#34;&#34;&#34;Return a single string representation of all linear interpolants.

        **print(lsq.toString())** produces the same visual output as
        **for line in lsq.toList(): print(line)**.
        &#34;&#34;&#34;
        i = 0
        s = &#34;&#34;
        for c in self.coef:
            s += (&#34;%d &lt;= x &lt; %d; y%d = %.3f + %.3fx; linear interpolation\n&#34;
                  % (self.x[i], self.x[i + 1],
                     i, c[0], c[1])
                  )
            i += 1
        return s</code></pre>
</details>
<h3>Methods</h3>
<dl>
<dt id="approximations.linear.__init__"><code class="name flex">
<span>def <span class="ident">__init__</span></span>(<span>self, dataset)</span>
</code></dt>
<dd>
<section class="desc"><p>Determine a linear interpolation between point i and i+1 for all i.</p></section>
<details class="source">
<summary>Source code</summary>
<pre><code class="python">def __init__(self, dataset):
    &#34;&#34;&#34;Determine a linear interpolation between point i and i+1 for all i.
    &#34;&#34;&#34;
    self.coef = []
    self.x = list(dataset.keys())

    x0, y0 = (None, None)
    x1, y1 = (None, None)

    for (x, y) in dataset.items():
        if x0 is None:
            x0, y0 = (x, y)
            continue
        x1, y1 = (x, y)
        c0 = y0 / (x0 - x1)
        c1 = y1 / (x1 - x0)
        px = npp([(-c0 * x1), c0]) + npp([(-c1 * x0), c1])
        px.coef.resize((1, 2))
        self.coef.append(px.coef[0])
        x0, y0 = (x, y)</code></pre>
</details>
</dd>
<dt id="approximations.linear.toList"><code class="name flex">
<span>def <span class="ident">toList</span></span>(<span>self)</span>
</code></dt>
<dd>
<section class="desc"><p>Return a list containing one string representation per linear interpolant.</p></section>
<details class="source">
<summary>Source code</summary>
<pre><code class="python">def toList(self):
    &#34;&#34;&#34;Return a list containing one string representation per linear interpolant.&#34;&#34;&#34;
    i = 0
    li = []
    for c in self.coef:
        li.append(&#34;%d &lt;= x &lt; %d; y%d = %.3f + %.fx; linear interpolation&#34;
                  % (self.x[i], self.x[i + 1], i, c[0], c[1])
                  )
        i += 1
    return li</code></pre>
</details>
</dd>
<dt id="approximations.linear.toString"><code class="name flex">
<span>def <span class="ident">toString</span></span>(<span>self)</span>
</code></dt>
<dd>
<section class="desc"><p>Return a single string representation of all linear interpolants.</p>
<p><strong>print(lsq.toString())</strong> produces the same visual output as
<strong>for line in lsq.toList(): print(line)</strong>.</p></section>
<details class="source">
<summary>Source code</summary>
<pre><code class="python">def toString(self):
    &#34;&#34;&#34;Return a single string representation of all linear interpolants.

    **print(lsq.toString())** produces the same visual output as
    **for line in lsq.toList(): print(line)**.
    &#34;&#34;&#34;
    i = 0
    s = &#34;&#34;
    for c in self.coef:
        s += (&#34;%d &lt;= x &lt; %d; y%d = %.3f + %.3fx; linear interpolation\n&#34;
              % (self.x[i], self.x[i + 1],
                 i, c[0], c[1])
              )
        i += 1
    return s</code></pre>
</details>
</dd>
</dl>
</dd>
</dl>
</section>
</article>
<nav id="sidebar">
<h1>Index</h1>
<div class="toc">
<ul></ul>
</div>
<ul id="index">
<li><h3><a href="#header-functions">Functions</a></h3>
<ul class="">
<li><code><a title="approximations.load_data" href="#approximations.load_data">load_data</a></code></li>
<li><code><a title="approximations.make_float" href="#approximations.make_float">make_float</a></code></li>
<li><code><a title="approximations.print_data" href="#approximations.print_data">print_data</a></code></li>
</ul>
</li>
<li><h3><a href="#header-classes">Classes</a></h3>
<ul>
<li>
<h4><code><a title="approximations.cubicSpline" href="#approximations.cubicSpline">cubicSpline</a></code></h4>
<ul class="">
<li><code><a title="approximations.cubicSpline.__init__" href="#approximations.cubicSpline.__init__">__init__</a></code></li>
<li><code><a title="approximations.cubicSpline.solve_matrix" href="#approximations.cubicSpline.solve_matrix">solve_matrix</a></code></li>
<li><code><a title="approximations.cubicSpline.toList" href="#approximations.cubicSpline.toList">toList</a></code></li>
<li><code><a title="approximations.cubicSpline.toString" href="#approximations.cubicSpline.toString">toString</a></code></li>
</ul>
</li>
<li>
<h4><code><a title="approximations.leastSquares" href="#approximations.leastSquares">leastSquares</a></code></h4>
<ul class="two-column">
<li><code><a title="approximations.leastSquares.__init__" href="#approximations.leastSquares.__init__">__init__</a></code></li>
<li><code><a title="approximations.leastSquares.basis_PI" href="#approximations.leastSquares.basis_PI">basis_PI</a></code></li>
<li><code><a title="approximations.leastSquares.make_row" href="#approximations.leastSquares.make_row">make_row</a></code></li>
<li><code><a title="approximations.leastSquares.make_row_b" href="#approximations.leastSquares.make_row_b">make_row_b</a></code></li>
<li><code><a title="approximations.leastSquares.sum_PIiPIj" href="#approximations.leastSquares.sum_PIiPIj">sum_PIiPIj</a></code></li>
<li><code><a title="approximations.leastSquares.toString" href="#approximations.leastSquares.toString">toString</a></code></li>
</ul>
</li>
<li>
<h4><code><a title="approximations.linear" href="#approximations.linear">linear</a></code></h4>
<ul class="">
<li><code><a title="approximations.linear.__init__" href="#approximations.linear.__init__">__init__</a></code></li>
<li><code><a title="approximations.linear.toList" href="#approximations.linear.toList">toList</a></code></li>
<li><code><a title="approximations.linear.toString" href="#approximations.linear.toString">toString</a></code></li>
</ul>
</li>
</ul>
</li>
</ul>
</nav>
</main>
<footer id="footer">
<p>Generated by <a href="https://pdoc3.github.io/pdoc"><cite>pdoc</cite> 0.5.4</a>.</p>
</footer>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.12.0/highlight.min.js"></script>
<script>hljs.initHighlightingOnLoad()</script>
</body>
</html>
