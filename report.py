from airium import Airium


class Student:
    def __init__(self, name, student_id, submission):
        self.name = name
        self.studentID = student_id
        self.submission = submission


class Submission:
    def __init__(self, submission_time, file_list):
        self.file_list = file_list
        self.submission_time = submission_time


class Submission_File:
    def __init__(self, code, name, id, scores, link):
        self.code = code
        self.name = name
        self.id = id
        self.qma_scores = [scores[0], scores[1], scores[2]]
        self.cma_scores = [scores[4], scores[3]]
        self.complexity_scores = scores[0]
        self.coupling_scores = scores[1]
        self.cohesion_scores = scores[2]
        self.naming_scores = scores[3]
        self.general_scores = scores[4]
        self.link = link


class Metric:
    def __init__(self, metric_names, metric_scores, instance_name, metric_category, metric_description):
        self.metric_names = metric_names
        self.metric_scores = metric_scores
        self.metric_category = metric_category
        self.instance_name = instance_name
        self.metric_description = metric_description
        self.base_score = metric_scores

    def set_scores(self, new_metric_scores):
        assert len(new_metric_scores) == len(self.metric_scores)
        self.metric_scores = new_metric_scores


complexity_metric_names = ['Cyclomatic Complexity (CC)', 'Lines of Code (LOC)', 'Weighted Methods per Class (WMC)', 'ABC']
coupling_metric_names = ['Coupling Factor (COF)', 'Coupling between objects (CBO)']
cohesion_metric_names = ['Depth of Inheritance (DIT)', 'Method Hiding Factor (MHF)', 'Attribute Hiding Factor (AHF)']
naming_metric_names = ['Class', 'Method', 'Attribute']
general_metric_names = ['Comment Percentage (CP)', 'Token Count (TC)']

complexity_metric_descriptions = ['The number of independent paths through the program.', 'The number of lines of code.', 'Number of control flow statements in the method.', 'Assignments, branches, and Conditionals.']
coupling_metric_descriptions = ['Degree of interdependence between modules.', 'Degree of interdependence objects.']
cohesion_metric_descriptions = ['The number of levels in the class hierarchy.', 'Extent to which a class hides same-signature methods.', 'Extent to which a class hides same-name attributes.']
naming_metric_descriptions = ['Extent to which a program follows class naming.', 'Extent to which a program follows method naming.', 'Extent to which a program follows attribute naming.']
general_metric_descriptions = ['Ratio of commented lines.', 'Number of keywords, identifiers, literals, and operators.']

complexity_metric_scores = [0, 9, 0, 0]
coupling_metric_scores = [0, 0]
cohesion_metric_scores = [0, 0, 0]
naming_metric_scores = [0, 0, 0]
general_metric_scores = [0, 0]

complexity = Metric(complexity_metric_names, complexity_metric_scores, 'complexity', 'Q', complexity_metric_descriptions)
coupling = Metric(coupling_metric_names, coupling_metric_scores, 'coupling', 'Q', coupling_metric_descriptions)
cohesion = Metric(cohesion_metric_names, cohesion_metric_scores, 'cohesion', 'Q', cohesion_metric_descriptions)
naming = Metric(naming_metric_names, naming_metric_scores, 'naming', 'C', naming_metric_descriptions)
general = Metric(general_metric_names, general_metric_scores, 'general', 'C', general_metric_descriptions)

metric_list = [complexity, naming, coupling, cohesion, general]
qma_metric_score_list = [complexity, coupling, cohesion]
cma_metric_score_list = [general, naming]

complexity_names = ['Cyclomatic Complexity (CC)', 'Lines of Code (LOC)', 'Weighted Methods per Class (WMC)', 'ABC']
coupling_names = ['Coupling Factor (COF)', 'Coupling between objects (CBO)']
cohesion_names = ['Depth of Inheritance (DIT)', 'Method Hiding Factor (MHF)', 'Attribute Hiding Factor (AHF)']

naming_names = ['Class', 'Method', 'Attribute']
general_names = ['Comment Percentage (CP)', 'Token Count (TC)']

cma_observation = ['one', 'two', 'three']
qma_observation = ['one', 'two', 'three']

student_list = []

assignment_link = ''

def create_student(name, student_id, submission):
    student = Student(name, student_id, submission)
    return student

def create_submission(submission_time, file_list):
    submission = Submission(submission_time, file_list)
    return submission

def create_file(code, name, id, scores, link):
    file = Submission_File(code, name, id, scores, link)
    return file

scores_1 = [complexity_metric_scores, cohesion_metric_scores, coupling_metric_scores, naming_metric_scores, general_metric_scores]
scores_2 = []
#code = 'import java.io.File;\n' + 'import java.io.FileNotFoundException;\n' + 'import java.util.Scanner;\n' + '\n' +'//\n' +'// DNAApp.java\n' +'//\n' +'// class to read in a file from the user and output the\n' +'//\n' +'// @author Kenneth Burt\n' +'//\n' +'public class DNAApp extends DNA1 {\n' +'\n' + '    public String Header;\n' +'    public String DNA = "";\n' +'    private String input;\n' +'\n' +'    public static void main(String[] args) throws FileNotFoundException {\n' +'\n' +'        Scanner keyBoard = new Scanner(System.in);\n' +'\n' +'        System.out.println("What is the name of the file?");\n' +'        input = keyBoard.nextLine();\n' +'\n' +'        File DNAFile = new File(input);\n' +'        Scanner DNAScan = new Scanner(DNAFile);\n' +'\n' +'        Header = DNAScan.nextLine();\n' +'\n' +'        int iterator = 2;\n' +'        while(DNAScan.hasNextLine()) {\n' +'            DNA = DNA + DNAScan.nextLine();\n' +'            iterator++;\n' +'        }\n' +'\n' +'        DNA ProteinCodes = new DNA(Header, DNA);\n' +'\n' +'        System.out.println(Header + "\\n" + ProteinCodes.getPCRs().toString());\n' +'    }\n' +'}\n'
language = "java"
#file_1 = create_file(code, 'file1', 123, scores_1, 'test1')
file_2 = create_file('test2', 'file2', 456, scores_1, 'test2')
#submission_1 = create_submission('December 30, 2022 at 9:37PM', [file_1, file_2])
#student_1 = create_student('Student 1', '123', submission_1)

file_3 = create_file('test3', 'file3', 789, scores_1, 'test3')
file_4 = create_file('test4', 'file4', 101112, scores_1, 'test4')
submission_2 = create_submission('December 30, 2022 at 9:37PM', [file_3, file_4])
student_2 = create_student('Student 2', '123', submission_2)

#student_list = [student_1, student_2]

#selected_student = student_list[0]
#focus_file = selected_student.submission.file_list[0]
#prev_student = student_1
#next_student = student_2

t = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]
threshold_list = t

def calc_scores_w_thresholds(t_):
    new_qma_metric_score_list = []
    for metric in qma_metric_score_list:
        for base, threshold in zip(metric.base_score, t_):
            new_value = 0
            if base <= 50:
                new_value = base - (threshold - 50)
            else:
                new_value = base + ((-1 * threshold) + 50)

            if new_value < 0:
                new_value = 0
            elif new_value > 100:
                new_value = 100

            new_qma_metric_score_list.append(new_value)
    print(new_qma_metric_score_list)


calc_scores_w_thresholds([100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100])
calc_scores_w_thresholds([0,0,0,0,0,0,0,0,0,0,0,0,0,0])
calc_scores_w_thresholds([50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50])


def go_here(guy, fill):
    print(student_list)
    selected_student = student_list[guy]
    focus_file = selected_student.submission.file_list[fill]

    prev_student = student_list[guy]
    next_student = student_list[guy]

    num = len(student_list)
    if guy + 1 < num:
        prev_student = student_list[guy+1]
    if guy != 0:
        next_student = student_list[guy-1]

    a = Airium()

    with a.head():
        a.title(_t='Title')
        a.script(src='https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.17/d3.js',
                 **{'data-require': 'd3@3.5.17', 'data-semver': '3.5.17'})
        a.script(src='https://rawgit.com/sujeetsr/d3.slider/master/d3.slider.js')
        a.script(src='https://cdn.amcharts.com/lib/4/core.js')
        a.script(src='https://cdn.amcharts.com/lib/4/charts.js')
        a.script(src='https://cdn.amcharts.com/lib/4/themes/animated.js')

    with a.script():
        a('var base_scores = [];\n\n    function open_cma_form() {\n        document.getElementById("cma_form").style.display = "block";\n        document.getElementById("main-page").style.display = "none";\n    }\n    function close_cma_form() {\n        document.getElementById("cma_form").style.display = "none";\n        document.getElementById("main-page").style.display = "block";\n    }\n    function open_qma_form() {\n        document.getElementById("qma_form").style.display = "block";\n        document.getElementById("main-page").style.display = "none";\n    }\n    function close_qma_form() {\n        document.getElementById("qma_form").style.display = "none";\n        document.getElementById("main-page").style.display = "block";\n    }\n\n    function open_pie_chart() {\n        document.getElementById("pie_chart_form").style.display = "block";\n        document.getElementById("main-page").style.display = "none";\n        //document.getElementById("chartdiv2").innerHTML = document.getElementById("chartdiv").innerHTML;\n    }\n    function close_pie_chart() {\n        document.getElementById("pie_chart_form").style.display = "none";\n        document.getElementById("main-page").style.display = "block";\n    }\n\n    function menu() {\n        document.getElementById("myDropdown").classList.toggle("show");\n    }\n    function change_secret(val, class_list){\n        let change_student_secret = document.getElementsByClassName("change_student_secret");\n        let slider_list = document.getElementsByClassName(\'slider-value\');\n        let change_file_secret_list = document.getElementsByClassName("change_file_secret");\n        let next_student_hidden_list = document.getElementsByClassName("next_student_hidden");\n        let prev_student_hidden_list = document.getElementsByClassName("prev_student_hidden");\n        for(let i = 0; i < change_file_secret_list.length; i++){\n            if(change_file_secret_list[i].classList.contains(class_list[0])){\n                change_file_secret_list[i].setAttribute("value", val);\n                //console.log(val);\n            }\n        }\n        for(let i=0; i < slider_list.length; i++){\n            if(slider_list[i].classList.contains(class_list[0])){\n                //change_student_secret[i].value = val;\n                change_student_secret[i].setAttribute("value",val)\n                console.log(change_student_secret[i].value);\n                next_student_hidden_list[i].setAttribute("value",val)\n                console.log(next_student_hidden_list[i].value);\n                prev_student_hidden_list[i].setAttribute("value",val)\n                console.log(prev_student_hidden_list[i].value);\n            }\n        }\n    }\n    function change_test(value, class_list){\n        //console.log(value);\n        let color_bar_value_list = document.getElementsByClassName("color_bar_value");\n        //let secret5_list = document.getElementsByClassName("secret5");\n        for (let i = 0; i < color_bar_value_list.length; i++) {\n            if(color_bar_value_list[i].classList.contains(class_list[0])){\n                color_bar_value_list[i].setAttribute("value", value)\n                //secret5_list[i].setAttribute("value", value)\n                //console.log(secret2_list[i].value)\n            }\n        }\n    }\n    function updateTextInput(parent) {\n        var new_threshold_value = -1;\n        for (const node of parent.childNodes) {\n            if(node.id === "rangeInput"){\n                new_threshold_value = node.value;\n                change_secret(new_threshold_value, node.classList);\n                let threshold_slider_class_list = node.classList.value;\n                let circle_list = document.getElementsByClassName("color-circle");\n                for(let i = 0; i < circle_list.length; i++){\n                    if(circle_list[i].classList.contains(threshold_slider_class_list)) {\n                        //console.log(\'match\')\n                        let base = base_scores[i];\n                        console.log(base_scores);\n                        let new_circle_value = 0;\n                        if(node.value < 50){\n                            new_circle_value = base - (node.value - 50)\n                        }else if (node.value > 50){\n                            new_circle_value = base + ((-1 * node.value) + 50)\n                        }else{\n                            new_circle_value = base\n                        }\n                        if(new_circle_value < 0){\n                            new_circle_value = 0;\n                        }else if (new_circle_value > 100){\n                            new_circle_value = 100\n                        }\n                        //console.log(new_circle_value)\n                        circle_list[i].style.setProperty(\'--value\', new_circle_value);\n                        change_test(new_circle_value, node.classList);\n                        loadFunction();\n                        break;\n                    }\n                }\n            }else if(node.id === "textInput"){\n                node.value = new_threshold_value;\n            }\n        }\n    }\n    function updateSlider(parent) {\n        var val = -1;\n        for (const node of parent.childNodes) {\n            if(node.id === "textInput"){\n                val = node.value;\n                if (val > 100){\n                    node.value = 100;\n                }\n            }\n        }\n        for (const node of parent.childNodes) {\n            if(node.id === "rangeInput"){\n                node.value = val;\n                let sv = node.value;\n                change_secret(sv, node.classList);\n                let slider_class_list = node.classList.value;\n                let circle_list = document.getElementsByClassName("color-circle");\n                let color_bar_value_list = document.getElementsByClassName("color_bar_value");\n                for(let i = 0; i < circle_list.length; i++){\n                    if(circle_list[i].classList.contains(slider_class_list)){\n                        let base = base_scores[i]\n                        let value = 0;\n                        if(sv <= 50){\n                            value = base - (sv - 50)\n                        }else if (sv > 50){\n                            value = base + ((-1 * sv) + 50)\n                        }\n\n                        if(value < 0){\n                            value = 0;\n                        }else if (value > 100){\n                            value = 100\n                        }\n                        circle_list[i].style.setProperty(\'--value\', value);\n                        change_test(value, node.classList);\n                        //color_bar_value_list[i].setAttribute(\'value\', value+\'\');\n                        loadFunction()\n                        break;\n                    }\n                }\n            }\n        }\n    }\n\n    //Regex functions for colored code - please leave in the {}\n    {\n        /* Rainbow v2.1.4 rainbowco.de | included languages: c, generic, java, javascript, python */ ! function(e, t) {\n        "object" == typeof exports && "undefined" != typeof module ? module.exports = t() : "function" == typeof define && define.amd ? define(t) : e.Rainbow = t()\n    }(this, function() {\n        "use strict";\n\n        function e() {\n            return "undefined" != typeof module && "object" == typeof module.exports\n        }\n\n        function t() {\n            return "undefined" == typeof document && "undefined" != typeof self\n        }\n\n        function n(e) {\n            var t = e.getAttribute("data-language") || e.parentNode.getAttribute("data-language");\n            if (!t) {\n                var n = /\\blang(?:uage)?-(\\w+)/,\n                    r = e.className.match(n) || e.parentNode.className.match(n);\n                r && (t = r[1])\n            }\n            return t ? t.toLowerCase() : null\n        }\n\n        function r(e, t, n, r) {\n            return (n !== e || r !== t) && (n <= e && r >= t)\n        }\n\n        function a(e) {\n            return e.replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/&(?![\\w\\#]+;)/g, "&amp;")\n        }\n\n        function o(e, t) {\n            for (var n = 0, r = 1; r < t; ++r) e[r] && (n += e[r].length);\n            return n\n        }\n\n        function i(e, t, n, r) {\n            return n >= e && n < t || r > e && r < t\n        }\n\n        function s(e) {\n            var t = [];\n            for (var n in e) e.hasOwnProperty(n) && t.push(n);\n            return t.sort(function(e, t) {\n                return t - e\n            })\n        }\n\n        function u(e, t, n, r) {\n            var a = r.substr(e);\n            return r.substr(0, e) + a.replace(t, n)\n        }\n\n        function c(t, Prism) {\n            if (e()) return global.Worker = require("webworker-threads").Worker, new Worker(__filename);\n            var n = Prism.toString(),\n                c = s.toString();\n            c += a.toString(), c += r.toString(), c += i.toString(), c += u.toString(), c += o.toString(), c += n;\n            var l = c + "\\tthis.onmessage=" + t.toString(),\n                f = new Blob([l], {\n                    type: "text/javascript"\n                });\n            return new Worker((window.URL || window.webkitURL).createObjectURL(f))\n        }\n\n        function l(e) {\n            function t() {\n                self.postMessage({\n                    id: n.id,\n                    lang: n.lang,\n                    result: a\n                })\n            }\n            var n = e.data,\n                r = new Prism(n.options),\n                a = r.refract(n.code, n.lang);\n            return n.isNode ? (t(), void self.close()) : void setTimeout(function() {\n                t()\n            }, 1e3 * n.options.delay)\n        }\n\n        function f() {\n            return (R || null === j) && (j = c(l, Prism)), j\n        }\n\n        function d(e, t) {\n            function n(a) {\n                a.data.id === e.id && (t(a.data), r.removeEventListener("message", n))\n            }\n            var r = f();\n            r.addEventListener("message", n), r.postMessage(e)\n        }\n\n        function g(e, t, n) {\n            return function(r) {\n                e.innerHTML = r.result, e.classList.remove("loading"), e.classList.add("rainbow-show"), "PRE" === e.parentNode.tagName && (e.parentNode.classList.remove("loading"), e.parentNode.classList.add("rainbow-show")), M && M(e, r.lang), 0 === --t.c && n()\n            }\n        }\n\n        function m(e) {\n            return {\n                patterns: C,\n                inheritenceMap: S,\n                aliases: T,\n                globalClass: e.globalClass,\n                delay: isNaN(e.delay) ? 0 : e.delay\n            }\n        }\n\n        function v(e, t) {\n            var n = {};\n            "object" == typeof t && (n = t, t = n.language), t = T[t] || t;\n            var r = {\n                id: A++,\n                code: e,\n                lang: t,\n                options: m(n),\n                isNode: R\n            };\n            return r\n        }\n\n        function p(e, t) {\n            for (var r = {\n                c: 0\n            }, a = 0, o = e; a < o.length; a += 1) {\n                var i = o[a],\n                    s = n(i);\n                if (!i.classList.contains("rainbow") && s) {\n                    i.classList.add("loading"), i.classList.add("rainbow"), "PRE" === i.parentNode.tagName && i.parentNode.classList.add("loading");\n                    var u = i.getAttribute("data-global-class"),\n                        c = parseInt(i.getAttribute("data-delay"), 10);\n                    ++r.c, d(v(i.innerHTML, {\n                        language: s,\n                        globalClass: u,\n                        delay: c\n                    }), g(i, r, t))\n                }\n            }\n            0 === r.c && t()\n        }\n\n        function h(e) {\n            var t = document.createElement("div");\n            t.className = "preloader";\n            for (var n = 0; n < 7; n++) t.appendChild(document.createElement("div"));\n            e.appendChild(t)\n        }\n\n        function b(e, t) {\n            t = t || function() {}, e = e && "function" == typeof e.getElementsByTagName ? e : document;\n            for (var n = e.getElementsByTagName("pre"), r = e.getElementsByTagName("code"), a = [], o = [], i = 0, s = n; i < s.length; i += 1) {\n                var u = s[i];\n                h(u), u.getElementsByTagName("code").length ? u.getAttribute("data-trimmed") || (u.setAttribute("data-trimmed", !0), u.innerHTML = u.innerHTML.trim()) : a.push(u)\n            }\n            for (var c = 0, l = r; c < l.length; c += 1) {\n                var f = l[c];\n                o.push(f)\n            }\n            p(o.concat(a), t)\n        }\n\n        function w(e) {\n            M = e\n        }\n\n        function y(e, t, n) {\n            S[e] || (S[e] = n), C[e] = t.concat(C[e] || [])\n        }\n\n        function L(e) {\n            delete S[e], delete C[e]\n        }\n\n        function N() {\n            for (var e = [], t = arguments.length; t--;) e[t] = arguments[t];\n            if ("string" == typeof e[0]) {\n                var n = v(e[0], e[1]);\n                return void d(n, function(e) {\n                    return function(t) {\n                        e && e(t.result, t.lang)\n                    }\n                }(e[2]))\n            }\n            return "function" == typeof e[0] ? void b(0, e[0]) : void b(e[0], e[1])\n        }\n\n        function E(e, t) {\n            T[e] = t\n        }\n        var M, Prism = function Prism(e) {\n                function t(e, t) {\n                    for (var n in h)\n                        if (n = parseInt(n, 10), r(n, h[n], e, t) && (delete h[n], delete p[n]), i(n, h[n], e, t)) return !0;\n                    return !1\n                }\n\n                function n(t, n) {\n                    var r = t.replace(/\\./g, " "),\n                        a = e.globalClass;\n                    return a && (r += " " + a), \'<span class="\' + r + \'">\' + n + "</span>"\n                }\n\n                function c(e) {\n                    for (var t = s(p), n = 0, r = t; n < r.length; n += 1) {\n                        var a = r[n],\n                            o = p[a];\n                        e = u(a, o.replace, o["with"], e)\n                    }\n                    return e\n                }\n\n                function l(e) {\n                    var t = "";\n                    return e.ignoreCase && (t += "i"), e.multiline && (t += "m"), new RegExp(e.source, t)\n                }\n\n                function f(r, a, i) {\n                    function c(e) {\n                        return r.name && (e = n(r.name, e)), p[w] = {\n                            replace: m[0],\n                            "with": e\n                        }, h[w] = y, !g && {\n                            remaining: a.substr(y - i),\n                            offset: y\n                        }\n                    }\n\n                    function f(t) {\n                        var a = m[t];\n                        if (a) {\n                            var i = r.matches[t],\n                                s = i.language,\n                                c = i.name && i.matches ? i.matches : i,\n                                l = function(e, r, a) {\n                                    b = u(o(m, t), e, a ? n(a, r) : r, b)\n                                };\n                            if ("string" == typeof i) return void l(a, a, i);\n                            var f, d = new Prism(e);\n                            if (s) return f = d.refract(a, s), void l(a, f);\n                            f = d.refract(a, v, c.length ? c : [c]), l(a, f, i.matches ? i.name : 0)\n                        }\n                    }\n                    void 0 === i && (i = 0);\n                    var d = r.pattern;\n                    if (!d) return !1;\n                    var g = !d.global;\n                    d = l(d);\n                    var m = d.exec(a);\n                    if (!m) return !1;\n                    !r.name && r.matches && "string" == typeof r.matches[0] && (r.name = r.matches[0], delete r.matches[0]);\n                    var b = m[0],\n                        w = m.index + i,\n                        y = m[0].length + w;\n                    if (w === y) return !1;\n                    if (t(w, y)) return {\n                        remaining: a.substr(y - i),\n                        offset: y\n                    };\n                    for (var L = s(r.matches), N = 0, E = L; N < E.length; N += 1) {\n                        var M = E[N];\n                        f(M)\n                    }\n                    return c(b)\n                }\n\n                function d(e, t) {\n                    for (var n = 0, r = t; n < r.length; n += 1)\n                        for (var a = r[n], o = f(a, e); o;) o = f(a, o.remaining, o.offset);\n                    return c(e)\n                }\n\n                function g(t) {\n                    for (var n = e.patterns[t] || []; e.inheritenceMap[t];) t = e.inheritenceMap[t], n = n.concat(e.patterns[t] || []);\n                    return n\n                }\n\n                function m(e, t, n) {\n                    return v = t, n = n || g(t), d(a(e), n)\n                }\n                var v, p = {},\n                    h = {};\n                this.refract = m\n            },\n            C = {},\n            S = {},\n            T = {},\n            x = {},\n            A = 0,\n            R = e(),\n            k = t(),\n            j = null;\n        x = {\n            extend: y,\n            remove: L,\n            onHighlight: w,\n            addAlias: E,\n            color: N\n        }, R && (x.colorSync = function(e, t) {\n            var n = v(e, t),\n                r = new Prism(n.options);\n            return r.refract(n.code, n.lang)\n        }), R || k || document.addEventListener("DOMContentLoaded", function(e) {\n            x.defer || x.color(e)\n        }, !1), k && (self.onmessage = l);\n        var B = x;\n        return B\n    });\n        Rainbow.extend("c", [{\n            name: "meta.preprocessor",\n            matches: {\n                1: [{\n                    matches: {\n                        1: "keyword.define",\n                        2: "entity.name"\n                    },\n                    pattern: /(\\w+)\\s(\\w+)\\b/g\n                }, {\n                    name: "keyword.define",\n                    pattern: /endif/g\n                }, {\n                    name: "constant.numeric",\n                    pattern: /\\d+/g\n                }, {\n                    matches: {\n                        1: "keyword.include",\n                        2: "string"\n                    },\n                    pattern: /(include)\\s(.*?)$/g\n                }]\n            },\n            pattern: /\\#([\\S\\s]*?)$/gm\n        }, {\n            name: "keyword",\n            pattern: /\\b(do|goto|typedef)\\b/g\n        }, {\n            name: "entity.label",\n            pattern: /\\w+:/g\n        }, {\n            matches: {\n                1: "storage.type",\n                3: "storage.type",\n                4: "entity.name.function"\n            },\n            pattern: /\\b((un)?signed|const)? ?(void|char|short|int|long|float|double)\\*? +((\\w+)(?= ?\\())?/g\n        }, {\n            matches: {\n                2: "entity.name.function"\n            },\n            pattern: /(\\w|\\*) +((\\w+)(?= ?\\())/g\n        }, {\n            name: "storage.modifier",\n            pattern: /\\b(static|extern|auto|register|volatile|inline)\\b/g\n        }, {\n            name: "support.type",\n            pattern: /\\b(struct|union|enum)\\b/g\n        }], "generic"), Rainbow.extend("generic", [{\n            matches: {\n                1: [{\n                    name: "keyword.operator",\n                    pattern: /\\=|\\+/g\n                }, {\n                    name: "keyword.dot",\n                    pattern: /\\./g\n                }],\n                2: {\n                    name: "string",\n                    matches: {\n                        name: "constant.character.escape",\n                        pattern: /\\\\(\'|"){1}/g\n                    }\n                }\n            },\n            pattern: /(\\(|\\s|\\[|\\=|:|\\+|\\.|\\{|,)((\'|")([^\\\\\\1]|\\\\.)*?(\\3))/gm\n        }, {\n            name: "comment",\n            pattern: /\\/\\*[\\s\\S]*?\\*\\/|(\\/\\/|\\#)(?!.*(\'|").*?[^:](\\/\\/|\\#)).*?$/gm\n        }, {\n            name: "constant.numeric",\n            pattern: /\\b(\\d+(\\.\\d+)?(e(\\+|\\-)?\\d+)?(f|d)?|0x[\\da-f]+)\\b/gi\n        }, {\n            matches: {\n                1: "keyword"\n            },\n            pattern: /\\b(and|array|as|b(ool(ean)?|reak)|c(ase|atch|har|lass|on(st|tinue))|d(ef|elete|o(uble)?)|e(cho|lse(if)?|xit|xtends|xcept)|f(inally|loat|or(each)?|unction)|global|if|import|int(eger)?|long|new|object|or|pr(int|ivate|otected)|public|return|self|st(ring|ruct|atic)|switch|th(en|is|row)|try|(un)?signed|var|void|while)(?=\\b)/gi\n        }, {\n            name: "constant.language",\n            pattern: /true|false|null/g\n        }, {\n            name: "keyword.operator",\n            pattern: /\\+|\\!|\\-|&(gt|lt|amp);|\\||\\*|\\=/g\n        }, {\n            matches: {\n                1: "function.call"\n            },\n            pattern: /(\\w+?)(?=\\()/g\n        }, {\n            matches: {\n                1: "storage.function",\n                2: "entity.name.function"\n            },\n            pattern: /(function)\\s(.*?)(?=\\()/g\n        }]), Rainbow.extend("java", [{\n            name: "constant",\n            pattern: /\\b(false|null|true|[A-Z_]+)\\b/g\n        }, {\n            matches: {\n                1: "keyword",\n                2: "support.namespace"\n            },\n            pattern: /(import|package)\\s(.+)/g\n        }, {\n            name: "keyword",\n            pattern: /\\b(abstract|assert|boolean|break|byte|case|catch|char|class|const|continue|default|do|double|else|enum|extends|final|finally|float|for|goto|if|implements|import|instanceof|int|interface|long|native|new|package|private|protected|public|return|short|static|strictfp|super|switch|synchronized|this|throw|throws|transient|try|void|volatile|while)\\b/g\n        }, {\n            name: "string",\n            pattern: /(".*?")/g\n        }, {\n            name: "char",\n            pattern: /(\')(.|\\\\.|\\\\u[\\dA-Fa-f]{4})\\1/g\n        }, {\n            name: "integer",\n            pattern: /\\b(0x[\\da-f]+|\\d+)L?\\b/g\n        }, {\n            name: "comment",\n            pattern: /\\/\\*[\\s\\S]*?\\*\\/|(\\/\\/).*?$/gm\n        }, {\n            name: "support.annotation",\n            pattern: /@\\w+/g\n        }, {\n            matches: {\n                1: "entity.function"\n            },\n            pattern: /([^@\\.\\s]+)\\(/g\n        }, {\n            name: "entity.class",\n            pattern: /\\b([A-Z]\\w*)\\b/g\n        }, {\n            name: "operator",\n            pattern: /(\\+{1,2}|-{1,2}|~|!|\\*|\\/|%|(?:&lt;){1,2}|(?:&gt;){1,3}|instanceof|(?:&amp;){1,2}|\\^|\\|{1,2}|\\?|:|(?:=|!|\\+|-|\\*|\\/|%|\\^|\\||(?:&lt;){1,2}|(?:&gt;){1,3})?=)/g\n        }]), Rainbow.extend("javascript", [{\n            name: "selector",\n            pattern: /\\$(?=\\.|\\()/g\n        }, {\n            name: "support",\n            pattern: /\\b(window|document)\\b/g\n        }, {\n            name: "keyword",\n            pattern: /\\b(export|default|from)\\b/g\n        }, {\n            name: "function.call",\n            pattern: /\\b(then)(?=\\()/g\n        }, {\n            name: "variable.language.this",\n            pattern: /\\bthis\\b/g\n        }, {\n            name: "variable.language.super",\n            pattern: /super(?=\\.|\\()/g\n        }, {\n            name: "storage.type",\n            pattern: /\\b(const|let|var)(?=\\s)/g\n        }, {\n            matches: {\n                1: "support.property"\n            },\n            pattern: /\\.(length|node(Name|Value))\\b/g\n        }, {\n            matches: {\n                1: "support.function"\n            },\n            pattern: /(setTimeout|setInterval)(?=\\()/g\n        }, {\n            matches: {\n                1: "support.method"\n            },\n            pattern: /\\.(getAttribute|replace|push|getElementById|getElementsByClassName|setTimeout|setInterval)(?=\\()/g\n        }, {\n            name: "string.regexp",\n            matches: {\n                1: "string.regexp.open",\n                2: {\n                    name: "constant.regexp.escape",\n                    pattern: /\\\\(.){1}/g\n                },\n                3: "string.regexp.close",\n                4: "string.regexp.modifier"\n            },\n            pattern: /(\\/)((?![*+?])(?:[^\\r\\n\\[\\/\\\\]|\\\\.|\\[(?:[^\\r\\n\\]\\\\]|\\\\.)*\\])+)(\\/)(?!\\/)([igm]{0,3})/g\n        }, {\n            matches: {\n                1: "storage.type",\n                3: "entity.function"\n            },\n            pattern: /(var)?(\\s|^)(\\S+)(?=\\s?=\\s?function\\()/g\n        }, {\n            matches: {\n                1: "keyword",\n                2: "variable.type"\n            },\n            pattern: /(new)\\s+(?!Promise)([^\\(]*)(?=\\()/g\n        }, {\n            name: "entity.function",\n            pattern: /(\\w+)(?=:\\s{0,}function)/g\n        }, {\n            name: "constant.other",\n            pattern: /\\*(?= as)/g\n        }, {\n            matches: {\n                1: "keyword",\n                2: "constant.other"\n            },\n            pattern: /(export)\\s+(\\*)/g\n        }, {\n            matches: {\n                1: "storage.type.accessor",\n                2: "entity.name.function"\n            },\n            pattern: /(get|set)\\s+(\\w+)(?=\\()/g\n        }, {\n            matches: {\n                2: "entity.name.function"\n            },\n            pattern: /(^\\s*)(\\w+)(?=\\([^\\)]*?\\)\\s*\\{)/gm\n        }, {\n            matches: {\n                1: "storage.type.class",\n                2: "entity.name.class",\n                3: "storage.modifier.extends",\n                4: "entity.other.inherited-class"\n            },\n            pattern: /(class)\\s+(\\w+)(?:\\s+(extends)\\s+(\\w+))?(?=\\s*\\{)/g\n        }, {\n            name: "storage.type.function.arrow",\n            pattern: /=&gt;/g\n        }, {\n            name: "support.class.promise",\n            pattern: /\\bPromise(?=(\\(|\\.))/g\n        }], "generic"), Rainbow.addAlias("js", "javascript"), Rainbow.extend("python", [{\n            name: "variable.self",\n            pattern: /self/g\n        }, {\n            name: "constant.language",\n            pattern: /None|True|False|NotImplemented|\\.\\.\\./g\n        }, {\n            name: "support.object",\n            pattern: /object/g\n        }, {\n            name: "support.function.python",\n            pattern: /\\b(bs|divmod|input|open|staticmethod|all|enumerate|int|ord|str|any|eval|isinstance|pow|sum|basestring|execfile|issubclass|print|super|bin|file|iter|property|tuple|bool|filter|len|range|type|bytearray|float|list|raw_input|unichr|callable|format|locals|reduce|unicode|chr|frozenset|long|reload|vars|classmethod|getattr|map|repr|xrange|cmp|globals|max|reversed|zip|compile|hasattr|memoryview|round|__import__|complex|hash|min|set|apply|delattr|help|next|setattr|buffer|dict|hex|object|slice|coerce|dir|id|oct|sorted|intern)(?=\\()/g\n        }, {\n            matches: {\n                1: "keyword"\n            },\n            pattern: /\\b(pass|lambda|with|is|not|in|from|elif|raise|del)(?=\\b)/g\n        }, {\n            matches: {\n                1: "storage.class",\n                2: "entity.name.class",\n                3: "entity.other.inherited-class"\n            },\n            pattern: /(class)\\s+(\\w+)\\((\\w+?)\\)/g\n        }, {\n            matches: {\n                1: "storage.function",\n                2: "support.magic"\n            },\n            pattern: /(def)\\s+(__\\w+)(?=\\()/g\n        }, {\n            name: "support.magic",\n            pattern: /__(name)__/g\n        }, {\n            matches: {\n                1: "keyword.control",\n                2: "support.exception.type"\n            },\n            pattern: /(except) (\\w+):/g\n        }, {\n            matches: {\n                1: "storage.function",\n                2: "entity.name.function"\n            },\n            pattern: /(def)\\s+(\\w+)(?=\\()/g\n        }, {\n            name: "entity.name.function.decorator",\n            pattern: /@([\\w\\.]+)/g\n        }, {\n            name: "comment.docstring",\n            pattern: /(\'{3}|"{3})[\\s\\S]*?\\1/gm\n        }], "generic");\n    }\n\n    function hslToHex(h, s, l) {\n        l /= 100;\n        const a = s * Math.min(l, 1 - l) / 100;\n        const f = n => {\n            const k = (n + h / 30) % 12;\n            const color = l - a * Math.max(Math.min(k - 3, 9 - k, 1), -1);\n            return Math.round(255 * color).toString(16).padStart(2, \'0\');   // convert to Hex and prefix "0" if needed\n        };\n        return `#${f(0)}${f(8)}${f(4)}`;\n    }\n\n    function loadFunction(){\n        base_scores = []\n        const newcircles= document.querySelectorAll(\'div[role="progressbar"]\');\n        for (let i = 0; i < newcircles.length; i++) {\n            newcircles[i].style.setProperty(\'--fg\', `hsl(${getComputedStyle(newcircles[i]).getPropertyValue(\'--value\')}, 100%, 50%)`)\n            newcircles[i].oninput =_=> newcircles[i].style.setProperty(\'--fg\', `hsl(${getComputedStyle(newcircles[i]).getPropertyValue(\'--value\')}, 100%, 50%)`)\n        }\n\n        var complexity_scores = ' + str(
            focus_file.complexity_scores) + '\n        var coupling_scores = ' + str(
            focus_file.coupling_scores) + '\n        var cohesion_scores = ' + str(
            focus_file.cohesion_scores) + '\n        var naming_scores = ' + str(
            focus_file.naming_scores) + '\n        var general_scores = ' + str(
            focus_file.general_scores) + '\n\n        base_scores = base_scores.concat(' + str(
            focus_file.complexity_scores) + ', ' + str(focus_file.coupling_scores) + ', ' + str(
            focus_file.cohesion_scores) + ', ' + str(focus_file.naming_scores) + ', ' + str(
            focus_file.general_scores) + ');\n\n        const score_list= document.querySelectorAll(\'td[class=score]\')\n        for (let i = 0; i < score_list.length; i++) {\n            //console.log(score_list[i].innerHTML)\n            let temp = Math.round(score_list[i].innerHTML / 10) * 10;\n            console.log(temp)\n            score_list[i].style.setProperty(\'background-color\', `hsl(${temp}, 100%, 50%)`)\n        }\n\n        am4core.ready(function() {\n            am4core.useTheme(am4themes_animated);\n\n            var chart = am4core.create("chartdiv", am4charts.PieChart);\n\n            // Let\'s cut a hole in our Pie chart the size of 40% the radius\n            chart.innerRadius = am4core.percent(40);\n            chart.data = [];\n            var chart_scale = 0.97;\n\n            let complexity = document.getElementsByClassName(\'complexity\');\n            let coupling = document.getElementsByClassName(\'coupling\');\n            let cohesion = document.getElementsByClassName(\'cohesion\');\n            let general = document.getElementsByClassName(\'general\');\n            let naming = document.getElementsByClassName(\'naming\');\n\n            chart.data = [];\n            let counter = 0;\n            for (let i = 0; i < complexity.length; i++) {\n                console.log(complexity[i].innerHTML.split(/\\r?\\n/)[1])\n                chart.data.push({\n                    "Complexity":complexity[i].innerHTML.split(/\\r?\\n/)[1] +\'\',\n                    "complexity_score":getComputedStyle(newcircles[counter]).getPropertyValue(\'--value\'),\n                    "color":am4core.color(hslToHex(getComputedStyle(newcircles[counter]).getPropertyValue(\'--value\'),100,50))\n                })\n                counter += 1;\n            }\n            for (let i = 0; i < coupling.length; i++) {\n                console.log(coupling[i].innerHTML.split(/\\r?\\n/)[1])\n                chart.data.push({\n                    "Coupling":coupling[i].innerHTML.split(/\\r?\\n/)[1] +\'\',\n                    "coupling_score":getComputedStyle(newcircles[counter]).getPropertyValue(\'--value\'),\n                    "color":am4core.color(hslToHex(getComputedStyle(newcircles[counter]).getPropertyValue(\'--value\'),100,50))\n                })\n                counter += 1;\n            }\n            for (let i = 0; i < cohesion.length; i++) {\n                console.log(cohesion[i].innerHTML.split(/\\r?\\n/)[1])\n                chart.data.push({\n                    "Cohesion":cohesion[i].innerHTML.split(/\\r?\\n/)[1] +\'\',\n                    "cohesion_score":getComputedStyle(newcircles[counter]).getPropertyValue(\'--value\'),\n                    "color":am4core.color(hslToHex(getComputedStyle(newcircles[counter]).getPropertyValue(\'--value\'),100,50))\n                })\n                counter += 1;\n            }\n            for (let i = 0; i < general.length; i++) {\n                console.log(general[i].innerHTML.split(/\\r?\\n/)[1])\n                chart.data.push({\n                    "General":general[i].innerHTML.split(/\\r?\\n/)[1] +\'\',\n                    "general_score":getComputedStyle(newcircles[counter]).getPropertyValue(\'--value\'),\n                    "color":am4core.color(hslToHex(getComputedStyle(newcircles[counter]).getPropertyValue(\'--value\'),100,50))\n                })\n                counter += 1;\n            }\n            for (let i = 0; i < naming.length; i++) {\n                console.log(naming[i].innerHTML.split(/\\r?\\n/)[1])\n                chart.data.push({\n                    "Naming":naming[i].innerHTML.split(/\\r?\\n/)[1] +\'\',\n                    "naming_score":getComputedStyle(newcircles[counter]).getPropertyValue(\'--value\'),\n                    "color":am4core.color(hslToHex(getComputedStyle(newcircles[counter]).getPropertyValue(\'--value\'),100,50))\n                })\n                counter += 1;\n            }\n\n            // Add and configure Series\n            var pieSeries = chart.series.push(new am4charts.PieSeries());\n            pieSeries.slices.template.propertyFields.fill = "color";\n            pieSeries.dataFields.value = "complexity_score";\n            pieSeries.dataFields.category = "Complexity";\n            pieSeries.slices.template.stroke = am4core.color("#fff");\n            pieSeries.slices.template.strokeWidth = 2;\n            pieSeries.slices.template.strokeOpacity = 1;\n            // Disabling labels and ticks on inner circle\n            pieSeries.labels.template.disabled = true;\n            pieSeries.ticks.template.disabled = true;\n            // Disable sliding out of slices\n            pieSeries.slices.template.states.getKey("hover").properties.shiftRadius = 0;\n            pieSeries.slices.template.states.getKey("hover").properties.scale = chart_scale;\n\n            // Add second series\n            var pieSeries2 = chart.series.push(new am4charts.PieSeries());\n            pieSeries2.slices.template.propertyFields.fill = "color";\n            pieSeries2.dataFields.value = "coupling_score";\n            pieSeries2.dataFields.category = "Coupling";\n            pieSeries2.slices.template.stroke = am4core.color("#fff");\n            pieSeries2.slices.template.strokeWidth = 2;\n            pieSeries2.slices.template.strokeOpacity = 1;\n            // Disabling labels and ticks on inner circle\n            pieSeries2.labels.template.disabled = true;\n            pieSeries2.ticks.template.disabled = true;\n            // Disable sliding out of slices\n            pieSeries2.slices.template.states.getKey("hover").properties.shiftRadius = 0;\n            pieSeries2.slices.template.states.getKey("hover").properties.scale = chart_scale;\n\n            var pieSeries3 = chart.series.push(new am4charts.PieSeries());\n            pieSeries3.slices.template.propertyFields.fill = "color";\n            pieSeries3.dataFields.value = "cohesion_score";\n            pieSeries3.dataFields.category = "Cohesion";\n            pieSeries3.slices.template.stroke = am4core.color("#fff");\n            pieSeries3.slices.template.strokeWidth = 2;\n            pieSeries3.slices.template.strokeOpacity = 1;\n            // Disabling labels and ticks on inner circle\n            pieSeries3.labels.template.disabled = true;\n            pieSeries3.ticks.template.disabled = true;\n            // Disable sliding out of slices\n            pieSeries3.slices.template.states.getKey("hover").properties.shiftRadius = 0;\n            pieSeries3.slices.template.states.getKey("hover").properties.scale = chart_scale;\n\n            var pieSeries4 = chart.series.push(new am4charts.PieSeries());\n            pieSeries4.slices.template.propertyFields.fill = "color";\n            pieSeries4.dataFields.value = "naming_score";\n            pieSeries4.dataFields.category = "Naming";\n            pieSeries4.slices.template.stroke = am4core.color("#fff");\n            pieSeries4.slices.template.strokeWidth = 2;\n            pieSeries4.slices.template.strokeOpacity = 1;\n            // Disabling labels and ticks on inner circle\n            pieSeries4.labels.template.disabled = true;\n            pieSeries4.ticks.template.disabled = true;\n            // Disable sliding out of slices\n            pieSeries4.slices.template.states.getKey("hover").properties.shiftRadius = 0;\n            pieSeries4.slices.template.states.getKey("hover").properties.scale = chart_scale;\n\n            var pieSeries5 = chart.series.push(new am4charts.PieSeries());\n            pieSeries5.slices.template.propertyFields.fill = "color";\n            pieSeries5.dataFields.value = "general_score";\n            pieSeries5.dataFields.category = "General";\n            pieSeries5.slices.template.stroke = am4core.color("#fff");\n            pieSeries5.slices.template.strokeWidth = 2;\n            pieSeries5.slices.template.strokeOpacity = 1;\n            // Disabling labels and ticks on inner circle\n            pieSeries5.labels.template.disabled = true;\n            pieSeries5.ticks.template.disabled = true;\n            // Disable sliding out of slices\n            pieSeries5.slices.template.states.getKey("hover").properties.shiftRadius = 0;\n            pieSeries5.slices.template.states.getKey("hover").properties.scale = chart_scale;\n\n            var chart2 = am4core.create("chartdiv2", am4charts.PieChart);\n\n            // Let\'s cut a hole in our Pie chart the size of 40% the radius\n            chart2.innerRadius = am4core.percent(40);\n\n            chart2.data = chart.data;\n\n            var pieSeriesBig = chart2.series.push(new am4charts.PieSeries());\n            pieSeriesBig.slices.template.propertyFields.fill = "color";\n            pieSeriesBig.dataFields.value = "complexity_score";\n            pieSeriesBig.dataFields.category = "Complexity";\n            pieSeriesBig.slices.template.stroke = am4core.color("#fff");\n            pieSeriesBig.slices.template.strokeWidth = 2;\n            pieSeriesBig.slices.template.strokeOpacity = 1;\n            // Disabling labels and ticks on inner circle\n            pieSeriesBig.labels.template.disabled = true;\n            pieSeriesBig.ticks.template.disabled = true;\n            // Disable sliding out of slices\n            pieSeriesBig.slices.template.states.getKey("hover").properties.shiftRadius = 0;\n            pieSeriesBig.slices.template.states.getKey("hover").properties.scale = chart_scale;\n\n            // Add second series\n            var pieSeriesBig2 = chart2.series.push(new am4charts.PieSeries());\n            pieSeriesBig2.slices.template.propertyFields.fill = "color";\n            pieSeriesBig2.dataFields.value = "coupling_score";\n            pieSeriesBig2.dataFields.category = "Coupling";\n            pieSeriesBig2.slices.template.stroke = am4core.color("#fff");\n            pieSeriesBig2.slices.template.strokeWidth = 2;\n            pieSeriesBig2.slices.template.strokeOpacity = 1;\n            // Disabling labels and ticks on inner circle\n            pieSeriesBig2.labels.template.disabled = true;\n            pieSeriesBig2.ticks.template.disabled = true;\n            // Disable sliding out of slices\n            pieSeriesBig2.slices.template.states.getKey("hover").properties.shiftRadius = 0;\n            pieSeriesBig2.slices.template.states.getKey("hover").properties.scale = chart_scale;\n\n            var pieSeriesBig3 = chart2.series.push(new am4charts.PieSeries());\n            pieSeriesBig3.slices.template.propertyFields.fill = "color";\n            pieSeriesBig3.dataFields.value = "cohesion_score";\n            pieSeriesBig3.dataFields.category = "Cohesion";\n            pieSeriesBig3.slices.template.stroke = am4core.color("#fff");\n            pieSeriesBig3.slices.template.strokeWidth = 2;\n            pieSeriesBig3.slices.template.strokeOpacity = 1;\n            // Disabling labels and ticks on inner circle\n            pieSeriesBig3.labels.template.disabled = true;\n            pieSeriesBig3.ticks.template.disabled = true;\n            // Disable sliding out of slices\n            pieSeriesBig3.slices.template.states.getKey("hover").properties.shiftRadius = 0;\n            pieSeriesBig3.slices.template.states.getKey("hover").properties.scale = chart_scale;\n\n            var pieSeriesBig4 = chart2.series.push(new am4charts.PieSeries());\n            pieSeriesBig4.slices.template.propertyFields.fill = "color";\n            pieSeriesBig4.dataFields.value = "naming_score";\n            pieSeriesBig4.dataFields.category = "Naming";\n            pieSeriesBig4.slices.template.stroke = am4core.color("#fff");\n            pieSeriesBig4.slices.template.strokeWidth = 2;\n            pieSeriesBig4.slices.template.strokeOpacity = 1;\n            // Disabling labels and ticks on inner circle\n            pieSeriesBig4.labels.template.disabled = true;\n            pieSeriesBig4.ticks.template.disabled = true;\n            // Disable sliding out of slices\n            pieSeriesBig4.slices.template.states.getKey("hover").properties.shiftRadius = 0;\n            pieSeriesBig4.slices.template.states.getKey("hover").properties.scale = chart_scale;\n\n            var pieSeriesBig5 = chart2.series.push(new am4charts.PieSeries());\n            pieSeriesBig5.slices.template.propertyFields.fill = "color";\n            pieSeriesBig5.dataFields.value = "general_score";\n            pieSeriesBig5.dataFields.category = "General";\n            pieSeriesBig5.slices.template.stroke = am4core.color("#fff");\n            pieSeriesBig5.slices.template.strokeWidth = 2;\n            pieSeriesBig5.slices.template.strokeOpacity = 1;\n            // Disabling labels and ticks on inner circle\n            pieSeriesBig5.labels.template.disabled = true;\n            pieSeriesBig5.ticks.template.disabled = true;\n            // Disable sliding out of slices\n            pieSeriesBig5.slices.template.states.getKey("hover").properties.shiftRadius = 0;\n            pieSeriesBig5.slices.template.states.getKey("hover").properties.scale = chart_scale;\n\n            chart2.legend = new am4charts.Legend();\n            chart2.legend.position = \'left\'\n            chart2.legend.maxWidth = 2000\n            chart2.legend.scrollable = true;\n        }); // end am4core.ready()\n\n    }\n\n    function showQMAPopup() {\n\n        document.getElementById(\'blackOverlay\').style.display = \'block\';\n        document.getElementById(\'qma_popup\').style.display = \'block\';\n\n    }\n\n    function closeQMAPopup() {\n\n        document.getElementById(\'blackOverlay\').style.display = \'none\';\n        document.getElementById(\'qma_popup\').style.display = \'none\';\n\n    }\n\n    function showCMAPopup() {\n\n        document.getElementById(\'blackOverlay\').style.display = \'block\';\n        document.getElementById(\'cma_popup\').style.display = \'block\';\n\n    }\n\n    function closeCMAPopup() {\n\n        document.getElementById(\'blackOverlay\').style.display = \'none\';\n        document.getElementById(\'cma_popup\').style.display = \'none\';\n\n    }\n\n    function showPiePopup() {\n\n        document.getElementById(\'blackOverlay\').style.display = \'block\';\n        document.getElementById(\'pie_popup\').style.display = \'block\';\n\n    }\n\n    function closePiePopup() {\n\n        document.getElementById(\'blackOverlay\').style.display = \'none\';\n        document.getElementById(\'pie_popup\').style.display = \'none\';\n\n    }\n\n\n    function submitForm(id, endpoint) {\n        var form = document.getElementById(id);\n        var xhr = new XMLHttpRequest();\n        xhr.open(\'POST\', endpoint, true);\n        xhr.setRequestHeader(\'Content-Type\', \'application/json\');\n        xhr.onreadystatechange = function() {\n            if (xhr.readyState === 4 && xhr.status === 200) {\n                console.log(xhr.responseText);\n                const response = JSON.parse(xhr.responseText);\n                // Assuming "bodyValue" is the key in the JSON response\n                document.body.innerHTML = response.bodyValue;\n            }\n        };\n        xhr.send(JSON.stringify(new FormData(form)));\n    }\n\n    window.addEventListener("DOMContentLoaded", (event) => {\n        document.getElementById("next_student_form").addEventListener("submit", function(event) {\n            event.preventDefault();\n            submitForm("next_student_form", "/next_student_endpoint");\n        });\n\n        document.getElementById("change_student_form").addEventListener("submit", function(event) {\n            event.preventDefault();\n            submitForm("change_student_form", "/change_student_endpoint");\n        });\n\n        document.getElementById("prev_student_form").addEventListener("submit", function(event) {\n            event.preventDefault();\n            submitForm("prev_student_form", "/prev_student_endpoint");\n        });\n\n    });')
    with a.style():
        a('body {\n        font: 14px "Lucida Grande", Helvetica, Arial, sans-serif;\n    }\n\n    #chartdiv2{\n        background-color: #f5f5f5;\n        height: 90%;\n    }\n\n    a {\n        color: #00B7FF;\n    }\n\n    p{\n        margin-left: 5%;\n        margin-top: 0;\n    }\n\n    b{\n        font-size: 14px;\n    }\n\n    th{\n        font-size: 16px;\n    }\n\n    #outer-grid {\n        display: grid;\n        grid-template-rows: 1fr 1fr;\n        grid-template-columns: 1fr 1fr 1fr 1fr;\n        grid-gap: 4px;\n        padding-top: 1px;\n    }\n    #outer-grid > div {\n        color: black;\n        padding: 2px;\n    }\n    #inner-grid {\n        display: grid;\n        grid-template-columns: 1fr;\n        grid-gap: 4px;\n    }\n    #inner-grid > div {\n        background: #f5f5f5;\n        border: #c7cdd1 solid;\n    }\n    th {\n        text-align: left;\n    }\n    .slider{\n        display: flex;\n    }\n    .slider-value{\n        text-align: center;\n        width: 10%;\n        height: 10%;\n        margin-top: auto;\n        margin-bottom: auto;\n        display: block;\n    }\n    .slidecontainer2 {\n        display: flex;\n    }\n    .slider2 {\n        --SliderColor: hsl(50, 100%, 50%);\n        -webkit-appearance: none;\n        height: 15px;\n        background-color: rgb(200, 200, 200);\n    }\n\n    /* --------------------------- webkit browsers */\n    .slider2::-webkit-slider-thumb {\n        -webkit-appearance: none;\n        width: 15px;\n        height: 15px;\n        background-color: var(--SliderColor);\n        overflow: visible;\n        cursor: pointer;\n    }\n    /* -------------------------- Firefox */\n    .slider2::-moz-range-thumb {\n        -moz-appearance: none;\n        width: 15px;\n        height: 15px;\n        border-radius: 10px;\n        background-color: var(--SliderColor);\n        overflow: visible;\n        cursor: pointer;\n    }\n    .slider2::-moz-focus-outer { border: 0; }\n    /* Remove dotted outline from range input element focused in Firefox */\n\n    #rangeInput {\n        -webkit-appearance: none;\n        height: 5px;\n        background: #d3d3d3;\n        justify-content: center;\n        opacity: 0.7;\n        -webkit-transition: .2s;\n        transition: opacity .2s;\n        margin-top: auto;\n        margin-bottom: auto;\n        margin-right: 5%;\n    }\n\n    #rangeInput::-webkit-slider-thumb {\n        -webkit-appearance: none;\n        appearance: none;\n        width: 15px;\n        height: 15px;\n        background: #5a5a5a;\n        border-radius:50px;\n        cursor: pointer;\n    }\n\n    #itr{\n        margin: auto;\n    }\n\n    input[type=\'range\'][id=\'itr\'] {\n        overflow: hidden;\n        width: auto;\n        -webkit-appearance: none;\n    }\n\n    input[type=\'range\'][id=\'itr\'] ::-webkit-slider-runnable-track {\n        height: 10px;\n        -webkit-appearance: none;\n        color: #13bba4;\n        margin-top: -1px;\n    }\n\n    input[type=\'range\']::-webkit-slider-thumb {\n        width: 1px;\n        -webkit-appearance: none;\n        height: 10px;\n        cursor: ew-resize;\n        box-shadow: -80px 0 0 80px var(--SliderColor);\n    }\n\n    .subheadContent {\n        display: flex;\n        justify-content: space-between;\n        align-items: center;\n        flex-wrap: nowrap;\n        background: rgba(57,75,88,255);\n        padding: 5px;\n    }\n\n    .subheadContent--flex-start {\n        display: flex;\n        justify-content: flex-start;\n        align-items: center;\n        flex-wrap: nowrap;\n        flex-shrink: 2;\n        min-width: 0;\n        padding-right: 12px;\n        overflow: hidden;\n    }\n\n    .gradebookActions {\n        display: flex;\n        align-items: center;\n        flex-wrap: nowrap;\n        margin-right: 12px;\n        flex-shrink: 0;\n    }\n\n    .a-style {\n        color: white;\n        text-decoration: none;\n    }\n\n    .assignmentDetails__Info {\n        font-size: 11px;\n        font-size: 0.6875rem;\n        font-weight: bold;\n        white-space: nowrap;\n        overflow: hidden;\n        text-overflow: ellipsis;\n        margin: 0;\n        padding: 0;\n        color: white;\n    }\n\n    .assignmentDetails__Title {\n        flex: 1;\n        min-width: 0;\n        font-size: 16px;\n        font-size: 1rem;\n        white-space: nowrap;\n        overflow: hidden;\n        text-overflow: ellipsis;\n        margin: 0;\n        padding: 0;\n    }\n\n    .subheadContent--flex-end {\n        display: flex;\n        align-items: center;\n        justify-content: flex-end;\n        flex-wrap: nowrap;\n        flex-shrink: 0;\n        min-width: 0;\n        padding-left: 12px;\n    }\n\n    .statsMetric {\n        display: flex;\n        align-items: center;\n        flex-wrap: nowrap;\n        align-self: flex-end;\n        padding-right: 12px;\n        border-right: 1px dotted var(--ic-brand-global-nav-menu-item__text-color);\n    }\n\n    .studentSelection {\n        display: flex;\n        align-items: center;\n        justify-content: flex-end;\n        flex-wrap: nowrap;\n        margin-left: 12px;\n    }\n\n    .statsMetric__Item {\n        display: flex;\n        flex-direction: column;\n        justify-content: center;\n        white-space: nowrap;\n        text-align: center;\n        margin-right: 24px;\n        color: white;\n    }\n\n    #gradebook_header #combo_box_container {\n        text-align: left;\n        background: transparent;\n    }\n\n    .navbar {\n        overflow: hidden;\n        background-color: #333;\n        font-family: Arial, Helvetica, sans-serif;\n    }\n\n    .navbar a {\n        float: left;\n        font-size: 16px;\n        color: white;\n        text-align: center;\n        padding: 14px 16px;\n        text-decoration: none;\n    }\n\n    .dropdown {\n        float: left;\n        overflow: hidden;\n    }\n\n    .dropdown .dropbtn {\n        cursor: pointer;\n        border: none;\n        outline: none;\n        color: white;\n        background-color: inherit;\n        font-family: inherit;\n        margin: 0;\n    }\n\n\n\n    /* Style the links inside the navigation bar */\n    .topnav a {\n        float: left;\n        display: block;\n        color: #f2f2f2;\n        text-align: center;\n        padding: 14px 16px;\n        text-decoration: none;\n        font-size: 17px;\n    }\n\n    /* Add an active class to highlight the current page */\n    .active {\n        background-color: #04AA6D;\n        color: white;\n    }\n\n    /* Hide the link that should open and close the topnav on small screens */\n    .topnav .icon {\n        display: none;\n    }\n\n    /* Dropdown container - needed to position the dropdown content */\n    .dropdown {\n        float: left;\n        overflow: hidden;\n    }\n\n\n    /* Style the dropdown content (hidden by default) */\n    .dropdown-content {\n        display: none;\n        position: absolute;\n        background-color: #f9f9f9;\n        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);\n        z-index: 1;\n    }\n\n    /* Style the links inside the dropdown */\n    .dropdown-content button{\n        float: none;\n        color: black;\n        text-decoration: none;\n        display: block;\n        text-align: left;\n    }\n\n\n    /* Add a grey background to dropdown links on hover */\n    .dropdown-content a:hover {\n        background-color: #ddd;\n        color: black;\n    }\n\n    .show {\n        display: block;\n    }\n\n    .gradebookMoveToNext {\n        padding: 0 12px;\n        background: transparent;\n        border: none;\n        cursor: pointer;\n        color: white;\n    }\n\n    .container {\n        width: 100%;\n    }\n\n    .clearfix {\n        overflow: auto;\n    }\n\n    .float-right {\n        float: right;\n    }\n\n    .ui-button {\n        background: #f5f5f5;\n        color: #2d3b45;\n        width: 100%;\n        border: 1px solid;\n        border-color: #c7cdd1;\n        border-radius: 3px;\n        transition: background-color .2s ease-in-out;\n        display: inline-block;\n        position: relative;\n        padding: 8px 14px;\n        margin-bottom: 0;\n        font-size: 16px;\n        font-size: 1rem;\n        line-height: 20px;\n        text-align: center;\n        vertical-align: middle;\n        cursor: pointer;\n        text-decoration: none;\n        overflow: hidden;\n        text-shadow: none;\n        -webkit-user-select: none;\n        user-select: none;\n    }\n\n    .student-selection-class{\n        background-color: #394b58;\n        border: none;\n        color: white\n    }\n\n    .other-student{\n        background-color: white;\n        color: black;\n    }\n    #submitted-file-list{\n    }\n    #submission-history{\n        padding-bottom: 10%;\n    }\n    .submission-file{\n        padding-bottom: 1%;\n        padding-left: 5%;\n        padding-right: 5%;\n    }\n\n    .secret{\n        display: none;\n    }\n\n    .secret2{\n        display: none;\n    }\n\n    .secret3{\n        display: none;\n    }\n\n    .summary-table table{\n        border: 1px solid #c7cdd1;\n        border-collapse: collapse;\n        table-layout: fixed ;\n        width: 100% ;\n    }\n\n    .summary-table th{\n        border: 1px solid #c7cdd1;\n        border-collapse: collapse;\n    }\n\n    .summary-table td{\n        border: 1px solid #c7cdd1;\n        border-collapse: collapse;\n        width: 25% ;\n    }\n\n    #outer-grid-summary{\n        display: grid;\n        grid-template-rows: 1fr 1fr;\n        grid-template-columns: 1fr;\n        grid-gap: 4px;\n        min-height: 100%\n    }\n\n    #outer-grid-summary > div {\n        color: black;\n    }\n\n    #inner-grid-summary{\n        display: grid;\n        grid-template-columns: 1fr;\n        grid-gap: 4px;\n    }\n\n    #inner-grid-summary > div {\n        background: #f5f5f5;\n        border: #c7cdd1 solid;\n    }\n\n    .submission_button{\n        border: none;\n        background: #f5f5f5;\n    }\n    .threshold-popup {\n        display: none;\n    }\n    .next_student_hidden{\n        display: none;\n    }\n    .prev_student_hidden{\n        display: none;\n    }\n    body{\n        padding: 0;\n        margin: 0;\n    }\n    body {\n        margin: 0;\n        font-family: \'Muli\', sans-serif;\n    }\n    .menu {\n        font-weight: 100;\n        background: #efefef;\n        width: 50%;\n        height: 100%;\n        top: -0.5%;\n        padding-left: 45px;\n        position: fixed;\n        z-index: 100;\n        -webkit-box-shadow: -3px 0 5px 0 rgba(0, 0, 0, 0.2);\n        box-shadow: -3px 0 5px 0 rgba(0, 0, 0, 0.2);\n        right: -50%;\n        transition: all 0.3s;\n        -webkit-transition: all 0.3s;\n        color: #222;\n    }\n    .menu:hover, .menu:focus {\n        transform: translate3d(-60%, 0, 0);\n        animation-timing-function: 1s ease-in;\n    }\n    .menu .title {\n        top: 50%;\n        position: absolute;\n        -webkit-transform: translateY(-50%);\n        -ms-transform: translateY(-50%);\n        transform: translateY(-50%);\n        transform: rotate(270deg);\n        left: -43px;\n        font-weight: 800;\n        font-size: 15px;\n    }\n\n    .menu .nav {\n        position: absolute;\n        top: 50%;\n        -webkit-transform: translateY(-50%);\n        -ms-transform: translateY(-50%);\n        transform: translateY(-50%);\n        font-weight: 100;\n        max-height:100%;\n        overflow-y: scroll;\n        padding-left: 0;\n    }\n\n    .menu .nav li {\n        list-style-type: none;\n    }\n    .nav{\n        width: 100%;\n    }\n\n    #outer-grid {\n        display: grid;\n        grid-template-rows: 1fr;\n        grid-template-columns: 3fr 2fr 1fr;\n        grid-auto-flow: column;\n        height: 100%;\n        padding: 4px;\n    }\n    #outer-grid > div {\n        background-color: white;\n        color: white;\n        padding: 4px;\n\n    }\n    #inner-grid {\n        display: grid;\n        grid-template-columns: 1fr;\n    }\n    #inner-grid > div {\n        background: #f5f5f5;\n        border: #c7cdd1 solid;\n        color: black;\n    }\n    .no-menu{\n        padding-right: 54px;\n    }\n\n    .next_student_hidden{\n        display: none;\n    }\n    .prev_student_hidden{\n        display: none;\n    }\n\n    .change_file_secret{\n        display: none;\n    }\n\n    .change_student_secret{\n        display: none;\n    }\n\n    .secret3{\n        display: none;\n    }\n\n    .studentSelection {\n        display: flex;\n        align-items: center;\n        flex-wrap: nowrap;\n        margin-left: 12px;\n        margin-right: 20%;\n    }\n\n    .subheadContent {\n        display: flex;\n        justify-content: space-between;\n        align-items: center;\n        flex-wrap: nowrap;\n        background: rgba(57,75,88,255);\n        padding: 7px;\n    }\n\n    .main-page{\n\n    }\n\n    .subheadContent--flex-start {\n        display: flex;\n        justify-content: flex-start;\n        align-items: center;\n        flex-wrap: nowrap;\n        flex-shrink: 2;\n        min-width: 0;\n        padding-right: 12px;\n        overflow: hidden;\n    }\n\n    .subheadContent--flex-end {\n        display: flex;\n        align-items: center;\n        justify-content: flex-end;\n        flex-wrap: nowrap;\n        flex-shrink: 0;\n        min-width: 0;\n        padding-left: 12px;\n    }\n\n    .gradebookActions {\n        display: flex;\n        align-items: center;\n        flex-wrap: nowrap;\n        margin-right: 12px;\n        flex-shrink: 0;\n    }\n\n    .a-style {\n        color: white;\n        text-decoration: none;\n    }\n\n\n    .statsMetric {\n        display: flex;\n        align-items: center;\n        flex-wrap: nowrap;\n        align-self: flex-end;\n        padding-right: 12px;\n        border-right: 1px dotted var(--ic-brand-global-nav-menu-item__text-color);\n    }\n\n    .gradebook_header{\n        z-index: 150;\n        position: relative;\n    }\n\n    .gradebookMoveToNext {\n        padding: 0 12px;\n        background: transparent;\n        border: none;\n        cursor: pointer;\n        color: white;\n    }\n\n    .student-selection-class{\n        background-color: #394b58;\n        border: none;\n        color: white;\n    }\n\n    #gradebook_header #combo_box_container {\n        text-align: left;\n        background: transparent;\n    }\n\n    .gradebookActions {\n        display: flex;\n        align-items: center;\n        flex-wrap: nowrap;\n        margin-right: 12px;\n        flex-shrink: 0;\n    }\n\n    .a-style {\n        color: white;\n        text-decoration: none;\n    }\n\n    .assignmentDetails__Info {\n        font-size: 11px;\n        font-size: 0.6875rem;\n        font-weight: bold;\n        white-space: nowrap;\n        overflow: hidden;\n        text-overflow: ellipsis;\n        margin: 0;\n        padding: 0;\n        color: white;\n    }\n\n    .assignmentDetails__Title {\n        flex: 1;\n        min-width: 0;\n        font-size: 16px;\n        font-size: 1rem;\n        white-space: nowrap;\n        overflow: hidden;\n        text-overflow: ellipsis;\n        margin: 0;\n        padding: 0;\n    }\n\n    .statsMetric {\n        display: flex;\n        align-items: center;\n        flex-wrap: nowrap;\n        align-self: flex-end;\n        padding-right: 12px;\n        border-right: 1px dotted var(--ic-brand-global-nav-menu-item__text-color);\n    }\n\n    .other-student{\n        background-color: white;\n        color: black;\n    }\n\n    form {\n        display: block;\n        margin: 0;\n    }\n\n    .circle {\n\n        background-color: #000;\n        border-radius: 0.8em;\n        -moz-border-radius: 0.8em;\n        -webkit-border-radius: 0.8em;\n        color: Black;\n        display: inline-block;\n        line-height: 1.6em;\n        text-align: center;\n        width: 1.6em;\n        border:1px solid gray;\n        box-shadow: 4px 2px 4px -4px black;\n    }\n\n    .grid-container {\n        display: grid;\n        gap: 0.25%;\n        grid-template-columns: repeat(7,minmax(0,1fr));\n        grid-template-rows: 45vh 45vh;\n        grid-template-areas:\n            \'code code code code qma_score qma_score file\'\n            \'code code code code qma_score qma_score file\';\n        background-color: white;\n        padding-right: 50px;\n        padding-top: 0.25%;\n        padding-bottom: 0.25%;\n\n    }\n    .item1 {\n        grid-area: code;\n        border: #c7cdd1 solid;\n        overflow: auto;\n        border-radius: 10px;\n    }\n    .item2 {\n        grid-area: qma_score;\n        background: #f5f5f5;\n        border: #c7cdd1 solid;\n        overflow: auto;\n        border-radius: 10px;\n        padding-top: 2%;\n        padding-left: 2%;\n    }\n    .item3 {\n        grid-area: cma_score;\n        background: #f5f5f5;\n        border: #c7cdd1 solid;\n        overflow: auto;\n        border-radius: 10px;\n    }\n    .item4 {\n        grid-area: file;\n        background: #f5f5f5;\n        border: #c7cdd1 solid;\n        border-radius: 10px;\n        padding-top: 2%;\n        padding-left: 2%;\n        padding-right: 2%;\n    }\n\n    .item5 {\n        grid-area: file2;\n        background: #f5f5f5;\n        border: #c7cdd1 solid;\n        border-radius: 10px;\n    }\n\n    .center-buttons{\n        text-align:center;\n        justify-content: center;\n    }\n\n    .button-padding{\n        padding: 1%;\n    }\n    .titles{\n        padding-top: 1%;\n        padding-bottom: 5%;\n    }\n\n    .qma-score-table  td{\n        font-size: 14px;\n    }\n\n    .qma-score-table  .table-title{\n        width: 90%;\n        padding-left: 5%;\n    }\n\n    .threshold-table-tab{\n        padding-left: 3%;\n    }\n\n    .qma-score-table{\n        padding-bottom: 5%;\n    }\n\n    .cma-score-table{\n        padding-bottom: 5%;\n    }\n\n    .threshold-table-content{\n        padding-left: 6%;\n        width: 40%;\n    }\n\n    .cma-score-table  td{\n        font-size: 14px;\n    }\n\n    .cma-score-table  .table-title{\n        width: 90%;\n        padding-left: 5%;\n    }\n\n    .threshold-table{\n        width: 70%;\n    }\n    .threshold-table td{\n        padding-bottom: 1%;\n    }\n\n    .progress-bar-cont{\n        text-align: center;\n    }\n\n    .metric-info-popup{\n        font-size: 10px;\n        z-index: 100;\n        position: absolute;\n        opacity: 0;\n    }\n\n    .cutoff {\n        text-overflow: ellipsis;\n        /* Required for text-overflow to do anything */\n        white-space: nowrap;\n        overflow: hidden;\n    }\n\n    .table-title p{\n        background: rgba(0, 0, 0, .75)\n        padding: 2px;\n        color: white;\n        border-radius: 0.8em;\n    }\n\n    .question:hover + p{\n        opacity: 1;\n    }\n\n    @keyframes growProgressBar {\n        0%, 33% { --pgPercentage: 0; }\n        100% { --pgPercentage: var(--value); }\n    }\n\n    @property --pgPercentage {\n        syntax: \'<number>\';\n        inherits: false;\n        initial-value: 0;\n    }\n\n    div[role="progressbar"] {\n        --size: 2rem;\n        --fg: #369;\n        --bg: #d9d9d9;\n        --pgPercentage: var(--value);\n        animation: growProgressBar 3s 1 forwards;\n        width: var(--size);\n        height: var(--size);\n        border-radius: 50%;\n        display: grid;\n        place-items: center;\n        background:\n                radial-gradient(closest-side, #f5f5f5 70%, transparent 0 99.9%, white 0),\n                conic-gradient(var(--fg) calc(var(--pgPercentage) * 1%), var(--bg) 0);\n        font-size: calc(var(--size) / 2);\n        font-weight: bold;\n        color: black;\n        box-shadow: 4px 2px 4px -4px black;\n    }\n\n    div[role="progressbar"]::before {\n        counter-reset: percentage var(--value);\n        content: counter(percentage);\n    }\n\n    .grid-title{\n        font-size: 18px;\n        font-weight: bold;\n    }\n    .ui-button-close{\n        background: #f5f5f5;\n        color: #2d3b45;\n        border: 3px #c7cdd1 solid;\n        transition: background-color .2s ease-in-out;\n        display: inline-block;\n        position: relative;\n        font-size: 14px;\n        text-align: center;\n        vertical-align: middle;\n        cursor: pointer;\n        text-decoration: none;\n        overflow: hidden;\n        text-shadow: none;\n        -webkit-user-select: none;\n        user-select: none;\n    }\n\n    .ui-button {\n        background: #f5f5f5;\n        color: #2d3b45;\n        border: 1px solid #c7cdd1;\n        border-radius: 3px;\n        transition: background-color .2s ease-in-out;\n        display: inline-block;\n        position: relative;\n        margin-bottom: 0;\n        font-size: 16px;\n        font-size: 1rem;\n        line-height: 20px;\n        text-align: center;\n        vertical-align: middle;\n        cursor: pointer;\n        text-decoration: none;\n        overflow: hidden;\n        text-shadow: none;\n        -webkit-user-select: none;\n        user-select: none;\n        margin-top: 5%;\n    }\n\n    .horizontal-center{\n        text-align: center;\n    }\n\n    ::-webkit-scrollbar {\n        width: 10px;\n        height: 10px;\n    }\n\n    /* Track */\n    ::-webkit-scrollbar-track {\n        box-shadow: inset 0 0 5px grey;\n        border-radius: 10px;\n    }\n\n    /* Handle */\n    ::-webkit-scrollbar-thumb {\n        background: #c7cdd1;\n        border-radius: 10px;\n    }\n\n    /* Handle on hover */\n    ::-webkit-scrollbar-thumb:hover {\n        background: #aaafb3;\n    }\n\n    .stacked{\n        display: block;\n    }\n\n    #submission-history{\n        padding-bottom: 10%;\n    }\n\n    #submission-files{\n        height: 75%;\n    }\n\n    .summary-container{\n        position: absolute;\n        width: 12.5%;\n        bottom:2%;\n    }\n\n    .pie_chart_button{\n        border: none;\n        background-color: #f5f5f5;\n        height: 100%;\n        width: 100%;\n    }\n\n    .pie_chart_popup{\n        display: none;\n    }\n\n    .center-pie-title{\n        justify-content: center;\n        display: flex;\n        background-color: #f5f5f5;\n        height: 10%;\n    }\n\n\n    .overlap {\n        position: absolute;\n        top: 50%;\n        left: 50%;\n        transform: translate(-50%, -50%);\n        z-index: 1000;\n    }\n\n    .summary-table td{\n        border: 1px solid #c7cdd1;\n        border-collapse: collapse;\n        width: 25% ;\n    }\n\n    .summary-table table{\n        border: 1px solid #c7cdd1;\n        border-collapse: collapse;\n        table-layout: fixed ;\n        width: 100% ;\n    }\n\n    .summary-table th{\n        border: 1px solid #c7cdd1;\n        border-collapse: collapse;\n    }\n\n    .threshold-popup {\n        display: none;\n    }\n\n    .blackOverlay {\n        display:none;\n        background:rgba(0,0,0,.6);\n        position:fixed;\n        top:0;\n        left:0;\n        width:100%;\n        height:100%;\n        z-index:200;\n    }\n\n    .popup {\n        display:none;\n        background:#fff;\n        position:fixed;\n        top:10%;\n        left:50%;\n        width:80%;\n        height:80%;\n        margin-left:-40%;\n        z-index:300;\n        border:2px solid #000;\n    }\n\n    .closePopup {\n        position: absolute;\n        right:0;\n        float:right;\n        font-weight:bold;\n        color:red;\n        cursor:pointer;\n    }\n\n\n\n    @keyframes fade-in{0%{opacity:0}100%{opacity:1}}@keyframes fade{10%{transform:scale(1, 1)}35%{transform:scale(1, 1.7)}40%{transform:scale(1, 1.7)}50%{opacity:1}60%{transform:scale(1, 1)}100%{transform:scale(1, 1);opacity:0}}[data-language] code,[class^="lang"] code,pre [data-language],pre [class^="lang"]{opacity:0;-ms-filter:"progid:DXImageTransform.Microsoft.Alpha(Opacity=100)";animation:fade-in 50ms ease-in-out 2s forwards}[data-language] code.rainbow,[class^="lang"] code.rainbow,pre [data-language].rainbow,pre [class^="lang"].rainbow{animation:none;transition:opacity 50ms ease-in-out}[data-language] code.loading,[class^="lang"] code.loading,pre [data-language].loading,pre [class^="lang"].loading{animation:none}[data-language] code.rainbow-show,[class^="lang"] code.rainbow-show,pre [data-language].rainbow-show,pre [class^="lang"].rainbow-show{opacity:1}pre{position:relative}pre.loading .preloader div{animation-play-state:running}pre.loading .preloader div:nth-of-type(1){background:#0081f5;animation:fade 1.5s 300ms linear infinite}pre.loading .preloader div:nth-of-type(2){background:#5000f5;animation:fade 1.5s 438ms linear infinite}pre.loading .preloader div:nth-of-type(3){background:#9000f5;animation:fade 1.5s 577ms linear infinite}pre.loading .preloader div:nth-of-type(4){background:#f50419;animation:fade 1.5s 715ms linear infinite}pre.loading .preloader div:nth-of-type(5){background:#f57900;animation:fade 1.5s 853ms linear infinite}pre.loading .preloader div:nth-of-type(6){background:#f5e600;animation:fade 1.5s 992ms linear infinite}pre.loading .preloader div:nth-of-type(7){background:#00f50c;animation:fade 1.5s 1130ms linear infinite}pre .preloader{position:absolute;top:12px;left:10px}pre .preloader div{width:12px;height:12px;border-radius:4px;display:inline-block;margin-right:4px;opacity:0;animation-play-state:paused;animation-fill-mode:forwards}pre{background-color:#000;word-wrap:break-word;margin:0px;padding:10px;color:#fff;font-size:16px;margin-bottom:20px}pre,code{font-family:\'Monaco\', \'Menlo\', courier, monospace}pre{background-color:#f5f5f5;color:#000000}pre .comment{color:#776e71}pre .variable.global,pre .variable.class,pre .variable.instance{color:#ef6155}pre .constant.numeric,pre .constant.language,pre .constant.hex-color,pre .keyword.unit{color:#f99b15}pre .constant,pre .entity,pre .entity.class,pre .support{color:#ff9500}pre .constant.symbol,pre .string{color:#00ff26}pre .entity.function,pre .support.css-property,pre .selector{color:#00bfff}pre .keyword,pre .storage{color:#bb00ff}')

    with a.body(onload='loadFunction()'):
        a.div(klass='blackOverlay', id='blackOverlay')
        with a.div(klass='subheadContent', id='gradebook_header'):
            with a.div(klass='subheadContent subheadContent--flex-start'):
                with a.div(klass='assignmentDetails'):
                    with a.a(klass='a-style', href=assignment_link, id='assignment_url'):
                        a.h2(klass='assignmentDetails__Title', _t='Test Comp Sci Java Assignment')
                    with a.p(klass='assignmentDetails__Info'):
                        a.span(_t='Due: 1/1, 2022 at 11:59')
                        a('-')
                        a.a(klass='a-style', href='/courses/2173881', id='context_title',
                            _t='CMPSC 404')
            with a.div(klass='subheadContent subheadContent--flex-end'):
                with a.div(klass='studentSelection'):
                    with a.form(action='http://127.0.0.1:5000/next_student', id='next_student_form', method='post'):
                        with a.label():
                            a.input(klass='secret3', name='next_student', value='123')
                        for i in range(
                                len(focus_file.coupling_scores + focus_file.cohesion_scores + focus_file.complexity_scores)):
                            with a.label():
                                a.input(klass='prev_student_hidden', name='prev_student_hidden',
                                        value=threshold_list[i])
                        for i in range(len(focus_file.general_scores + focus_file.naming_scores)):
                            with a.label():
                                a.input(klass='prev_student_hidden', name='prev_student_hidden', value=threshold_list[
                                    i + len(focus_file.coupling_scores) + len(focus_file.cohesion_scores) + len(
                                        focus_file.complexity_scores)])

                        with a.button(klass='Button Button--icon-action gradebookMoveToNext prev',
                                      id='prev-student-button',
                                      type='submit', **{'aria-label': 'Previous'}):
                            with a.svg(klass='bi bi-arrow-left-short', fill='currentColor', height='16',
                                       viewbox='0 0 16 16', width='16', xmlns='http://www.w3.org/2000/svg'):
                                a.path(
                                    d='M12 8a.5.5 0 0 1-.5.5H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5H11.5a.5.5 0 0 1 .5.5z',
                                    **{'fill-rule': 'evenodd'})
                    with a.form(action='http://127.0.0.1:5000/change_student', id='change_student_form', method='post'):
                        with a.select(klass='student-selection-class', id='student-list', name='student_list',
                                      onchange='this.form.submit()'):
                            for i in range(len(student_list)):
                                if selected_student == student_list[i]:
                                    a.option(klass='other-student', selected='', value=student_list[i].studentID,
                                             _t=student_list[i].name)
                                else:
                                    a.option(klass='other-student', value=student_list[i].studentID,
                                             _t=student_list[i].name)
                        for i in range(
                                len(focus_file.coupling_scores + focus_file.cohesion_scores + focus_file.complexity_scores)):
                            with a.label():
                                a.input(klass='change_student_secret', name='test', value=threshold_list[i])
                        for i in range(len(focus_file.general_scores + focus_file.naming_scores)):
                            with a.label():
                                a.input(klass='change_student_secret', name='test', value=threshold_list[
                                    i + len(focus_file.coupling_scores) + len(focus_file.cohesion_scores) + len(
                                        focus_file.complexity_scores)])

                    with a.form(action='http://127.0.0.1:5000/next_student', id='prev_student_form', method='post'):
                        with a.label():
                            a.input(klass='secret3', name='next_student', value='456')
                        with a.button(klass='Button Button--icon-action gradebookMoveToNext next',
                                      id='next-student-button',
                                      type='submit', **{'aria-label': 'Next'}):
                            with a.svg(klass='bi bi-arrow-right-short', fill='currentColor', height='16',
                                       viewbox='0 0 16 16', width='16', xmlns='http://www.w3.org/2000/svg'):
                                a.path(
                                    d='M4 8a.5.5 0 0 1 .5-.5h5.793L8.146 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708-.708L10.293 8.5H4.5A.5.5 0 0 1 4 8z',
                                    **{'fill-rule': 'evenodd'})
                        for i in range(
                                len(focus_file.coupling_scores + focus_file.cohesion_scores + focus_file.complexity_scores)):
                            with a.label():
                                a.input(klass='next_student_hidden', name='next_student_hidden',
                                        value=threshold_list[i])
                        for i in range(len(focus_file.general_scores + focus_file.naming_scores)):
                            with a.label():
                                a.input(klass='next_student_hidden', name='next_student_hidden', value=threshold_list[
                                    i + len(focus_file.coupling_scores) + len(focus_file.cohesion_scores) + len(
                                        focus_file.complexity_scores)])
        a.div(klass='blackOverlay', id='blackOverlay')
        with a.div(klass='popup', id='qma_popup'):
            a.button(klass='closePopup ui-button-close', onclick='closeQMAPopup()', type='button', _t='X')
            with a.div(klass='qma-popup', id='qma_form'):
                with a.div(id='outer-grid-summary'):
                    with a.div(id='inner-grid-summary'):
                        with a.div(klass='summary-table'):
                            with a.table():
                                with a.tr():
                                    a.th(colspan='12', _t='Quality Metric Analysis Report')
                                with a.tr():
                                    a.th(colspan='3')
                                    a.th(colspan=len(complexity_names), _t='Complexity')
                                    a.th(colspan=len(coupling_names), _t='Coupling')
                                    a.th(colspan=len(cohesion_names), _t='Cohesion')
                                with a.tr():
                                    a.td(_t='Student Name')
                                    a.td(_t='Student ID')
                                    a.td(_t='File')
                                    for i in range(len(complexity_names)):
                                        a.td(_t=complexity_names[i])
                                    for i in range(len(coupling_names)):
                                        a.td(_t=coupling_names[i])
                                    for i in range(len(cohesion_names)):
                                        a.td(_t=cohesion_names[i])
                                for i in range(len(student_list)):
                                    for j in range(len(student_list[i].submission.file_list)):
                                        with a.tr():
                                            if j == 0:
                                                a.td(_t=student_list[i].name)
                                                a.td(_t=student_list[i].studentID)
                                            else:
                                                a.td()
                                                a.td()
                                            a.td(klass='cutoff', _t=student_list[i].submission.file_list[j].name)
                                            for k in range(len(student_list[i].submission.file_list[j].complexity_scores)):
                                                a.td(klass='score',_t=str(student_list[i].submission.file_list[j].complexity_scores[k]))
                                            for k in range(len(student_list[i].submission.file_list[j].coupling_scores)):
                                                a.td(klass='score',_t=str(student_list[i].submission.file_list[j].coupling_scores[k]))
                                            for k in range(len(student_list[i].submission.file_list[j].cohesion_scores)):
                                                a.td(klass='score', _t=str(student_list[i].submission.file_list[j].cohesion_scores[k]))
                    with a.div(id='inner-grid-summary'):
                        with a.div():
                            with a.table():
                                with a.tr():
                                    a.th(colspan='2', _t='QMA Summary Observations')
                                for i in range(len(qma_observation)):
                                    with a.tr():
                                        a.td(_t=qma_observation[i])
        with a.div(klass='popup', id='cma_popup'):
            a.button(klass='closePopup ui-button-close', onclick='closeCMAPopup()', type='button', _t='X')
            with a.div(klass='cma-popup', id='cma_form'):
                with a.div(id='outer-grid-summary'):
                    with a.div(id='inner-grid-summary'):
                        with a.div(klass='summary-table'):
                            with a.table():
                                with a.tr():
                                    a.th(colspan='8', _t='Convention Metric Analysis Report')
                                with a.tr():
                                    a.th(colspan='3')
                                    a.th(colspan='2', _t='General')
                                    a.th(colspan='3', _t='Naming Conventions')
                                with a.tr():
                                    a.td(_t='Student Name')
                                    a.td(_t='Student ID')
                                    a.td(_t='File')
                                    for i in range(len(general_names)):
                                        a.td(_t=general_names[i])
                                    for i in range(len(naming_names)):
                                        a.td(_t=naming_names[i])
                                for i in range(len(student_list)):
                                    for j in range(len(student_list[i].submission.file_list)):
                                        with a.tr():
                                            if j == 0:
                                                a.td(_t=student_list[i].name)
                                                a.td(_t=student_list[i].studentID)
                                            else:
                                                a.td()
                                                a.td()
                                            a.td(klass='cutoff', _t=student_list[i].submission.file_list[j].name)
                                            for k in range(len(student_list[i].submission.file_list[j].general_scores)):
                                                a.td(klass='score',_t=str(student_list[i].submission.file_list[j].general_scores[k]))
                                            for k in range(len(student_list[i].submission.file_list[j].naming_scores)):
                                                a.td(klass='score',_t=str(student_list[i].submission.file_list[j].naming_scores[k]))
                    with a.div(id='inner-grid-summary'):
                        with a.div():
                            with a.table():
                                with a.tr():
                                    a.th(colspan='2', _t='CMA Summary Observations')
                                for i in range(len(cma_observation)):
                                    with a.tr():
                                        a.td(_t=cma_observation[i])

        with a.div(klass='popup', id='pie_popup'):
            with a.button(klass='pie_chart_button', onclick='closePiePopup()'):
                with a.div(klass='center-pie-title'):
                    a.h1(_t='Metric Analysis (Click to Close)')
                a.div(id='chartdiv2')
        with a.div(id='main-page'):
            with a.div(klass='menu'):
                with a.div(klass='title'):
                    a('THRESHOLDS')
                    with a.svg(klass='bi bi-caret-up-fill', fill='currentColor', height='16', viewbox='0 0 16 16',
                               width='16', xmlns='http://www.w3.org/2000/svg'):
                        a.path(
                            d='m7.247 4.86-4.796 5.481c-.566.647-.106 1.659.753 1.659h9.592a1 1 0 0 0 .753-1.659l-4.796-5.48a1 1 0 0 0-1.506 0z')
                with a.ul(klass='nav'):
                    with a.li(style='padding-top: 5%;'):
                        with a.div():
                            with a.span():
                                a.b(_t='QMA Thresholds')
                    counter = 0
                    with a.li():
                        with a.table(klass='threshold-table'):
                            for i in range(len(qma_metric_score_list)):
                                with a.tr():
                                    with a.td(klass='threshold-table-tab'):
                                        a.b(_t=qma_metric_score_list[i].instance_name)
                                for j in range(len(qma_metric_score_list[i].metric_scores)):
                                    with a.tr():
                                        a.td(klass='threshold-table-content',
                                             _t=qma_metric_score_list[i].metric_names[j])
                                        with a.td():
                                            with a.div(klass='slider qma-threshold-update'):
                                                a.input(klass='s' + str(counter + 1), id='rangeInput', max='100',
                                                        min='0',
                                                        name='rangeInput', onchange='updateTextInput(this.parentNode);',
                                                        type='range', value=threshold_list[counter])
                                                a.input(klass='slider-value s' + str(counter + 1), id='textInput',
                                                        onchange='updateSlider(this.parentNode);', type='text',
                                                        value=threshold_list[counter])
                                    counter += 1
                    with a.li():
                        with a.div():
                            with a.span():
                                a.b(_t='CMA Thresholds')
                    with a.li(style='padding-bottom: 5%;'):
                        with a.table(klass='threshold-table'):
                            for i in range(len(cma_metric_score_list)):
                                with a.tr():
                                    with a.td(klass='threshold-table-tab'):
                                        a.b(_t=cma_metric_score_list[i].instance_name)
                                for j in range(len(cma_metric_score_list[i].metric_scores)):
                                    with a.tr():
                                        a.td(klass='threshold-table-content',
                                             _t=cma_metric_score_list[i].metric_names[j])
                                        with a.td():
                                            with a.div(klass='slider qma-threshold-update'):
                                                a.input(klass='s' + str(counter + 1), id='rangeInput', max='100',
                                                        min='0',
                                                        name='rangeInput', onchange='updateTextInput(this.parentNode);',
                                                        type='range', value=threshold_list[counter])
                                                a.input(klass='slider-value s' + str(counter + 1), id='textInput',
                                                        onchange='updateSlider(this.parentNode);', type='text',
                                                        value=threshold_list[counter])
                                    counter += 1
            with a.div(klass='grid-container'):
                with a.div(klass='item1', style='background-color: #f5f5f5'):
                    a.pre(_t='<code data-language="' + language + '" id="file-code">' + focus_file.code + '</code>')
                with a.div(klass='item2'):
                    with a.div():
                        a.span(klass='grid-title', _t='Quality Metric Analysis (QMA)')
                    with a.table(klass='qma-score-table'):
                        counter = 0
                        for i in range(len(qma_metric_score_list)):
                            with a.tr():
                                with a.td():
                                    a.b(_t=qma_metric_score_list[i].instance_name)
                            for j in range(len(qma_metric_score_list[i].metric_scores)):
                                with a.tr():
                                    with a.td(klass='table-title ' + qma_metric_score_list[i].instance_name):
                                        a(qma_metric_score_list[i].metric_names[j])
                                        with a.svg(klass='bi bi-question-circle question', fill='currentColor',
                                                   height='16',
                                                   viewbox='0 0 16 16', width='16', xmlns='http://www.w3.org/2000/svg'):
                                            a.path(
                                                d='M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z')
                                            a.path(
                                                d='M5.255 5.786a.237.237 0 0 0 .241.247h.825c.138 0 .248-.113.266-.25.09-.656.54-1.134 1.342-1.134.686 0 1.314.343 1.314 1.168 0 .635-.374.927-.965 1.371-.673.489-1.206 1.06-1.168 1.987l.003.217a.25.25 0 0 0 .25.246h.811a.25.25 0 0 0 .25-.25v-.105c0-.718.273-.927 1.01-1.486.609-.463 1.244-.977 1.244-2.056 0-1.511-1.276-2.241-2.673-2.241-1.267 0-2.655.59-2.75 2.286zm1.557 5.763c0 .533.425.927 1.01.927.609 0 1.028-.394 1.028-.927 0-.552-.42-.94-1.029-.94-.584 0-1.009.388-1.009.94z')
                                        a.p(klass='metric-info-popup',
                                            _t=qma_metric_score_list[i].metric_description[j])
                                    with a.td(klass='progress-bar-cont'):
                                        a.div(klass='color-circle s' + str(counter + 1), role='progressbar',
                                              style='--value:' + str(focus_file.qma_scores[i][j]),
                                              **{'aria-valuemax': '100', 'aria-valuemin': '0', 'aria-valuenow': '65'})
                                counter += 1

                    with a.div():
                        a.span(klass='grid-title', _t='Convention Metric Analysis (CMA)')
                    with a.table(klass='cma-score-table'):
                        for i in range(len(cma_metric_score_list)):
                            with a.tr():
                                with a.td():
                                    a.b(_t=cma_metric_score_list[i].instance_name)
                            for j in range(len(cma_metric_score_list[i].metric_scores)):
                                with a.tr():
                                    with a.td(klass='table-title ' + cma_metric_score_list[i].instance_name):
                                        a(cma_metric_score_list[i].metric_names[j])
                                        with a.svg(klass='bi bi-question-circle question', fill='currentColor',
                                                   height='16',
                                                   viewbox='0 0 16 16', width='16', xmlns='http://www.w3.org/2000/svg'):
                                            a.path(
                                                d='M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z')
                                            a.path(
                                                d='M5.255 5.786a.237.237 0 0 0 .241.247h.825c.138 0 .248-.113.266-.25.09-.656.54-1.134 1.342-1.134.686 0 1.314.343 1.314 1.168 0 .635-.374.927-.965 1.371-.673.489-1.206 1.06-1.168 1.987l.003.217a.25.25 0 0 0 .25.246h.811a.25.25 0 0 0 .25-.25v-.105c0-.718.273-.927 1.01-1.486.609-.463 1.244-.977 1.244-2.056 0-1.511-1.276-2.241-2.673-2.241-1.267 0-2.655.59-2.75 2.286zm1.557 5.763c0 .533.425.927 1.01.927.609 0 1.028-.394 1.028-.927 0-.552-.42-.94-1.029-.94-.584 0-1.009.388-1.009.94z')
                                        a.p(klass='metric-info-popup',
                                            _t=cma_metric_score_list[i].metric_description[j])
                                    with a.td(klass='progress-bar-cont'):
                                        a.div(klass='color-circle s' + str(counter + 1), role='progressbar',
                                              style='--value:' + str(focus_file.cma_scores[i][j]),
                                              **{'aria-valuemax': '100', 'aria-valuemin': '0', 'aria-valuenow': '65'})
                                counter += 1
                    with a.div():
                        a.span(klass='grid-title', _t='Metric Analysis (Click to Expand)')
                    with a.button(klass='pie_chart_button', onclick='showPiePopup()',
                                  style='width: 90%; height: 40%; margin-left: 5%'):
                        a.div(id='chartdiv')
                with a.div(klass='item4'):
                    with a.div():
                        with a.div(id='submission-details'):
                            with a.div(id='submission-history'):
                                with a.label():
                                    a.b(_t='Submitted:')
                                a('December 30, 2022 at 9:37PM')
                            with a.div(id='submission-files'):
                                with a.label():
                                    a.b(_t='Submitted Files:')
                                a.span(_t='(Click to load)')
                                with a.div(id='submitted-file-list'):
                                    for i in range(len(selected_student.submission.file_list)):
                                        with a.div(klass='submission-file'):
                                            with a.div(klass='container'):
                                                with a.form(action='http://127.0.0.1:5000/change_file',
                                                            klass='file_form_test', id='file_form', method='post'):
                                                    a.button(klass='submission_button',
                                                             name=str(selected_student.submission.file_list[
                                                                          i].id) + '-' + str(
                                                                 selected_student.studentID), type='submit',
                                                             _t=selected_student.submission.file_list[i].name)
                                                    with a.label():
                                                        a.input(klass='change_file_secret', name='student_id',
                                                                value=selected_student.studentID)
                                                    with a.label():
                                                        a.input(klass='change_file_secret', name='file_id',
                                                                value=selected_student.submission.file_list[i].id)
                                                    counter = 0
                                                    for j in range(len(qma_metric_score_list)):
                                                        for l in range(len(qma_metric_score_list[j].metric_scores)):
                                                            with a.label():
                                                                a.input(klass='s' + str(
                                                                    counter + 1) + ' change_file_secret file_threshold',
                                                                        name='fuck', value=threshold_list[counter])
                                                            counter += 1
                                                    for j in range(len(cma_metric_score_list)):
                                                        for l in range(len(cma_metric_score_list[j].metric_scores)):
                                                            with a.label():
                                                                a.input(klass='s' + str(
                                                                    counter + 1) + ' change_file_secret file_threshold',
                                                                        name='fuck', value=threshold_list[counter])
                                                            counter += 1
                                                    with a.a(klass='submission-file-download icon-download float-right',
                                                             download='',
                                                             href=selected_student.submission.file_list[i].link):
                                                        with a.span(klass='screenreader-only'):
                                                            with a.svg(klass='bi bi-download', fill='currentColor',
                                                                       height='16', viewbox='0 0 16 16', width='16',
                                                                       xmlns='http://www.w3.org/2000/svg'):
                                                                a.path(
                                                                    d='M.5 9.9a.5.5 0 0 1 .5.5v2.5a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2.5a.5.5 0 0 1 1 0v2.5a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2v-2.5a.5.5 0 0 1 .5-.5z')
                                                                a.path(
                                                                    d='M7.646 11.854a.5.5 0 0 0 .708 0l3-3a.5.5 0 0 0-.708-.708L8.5 10.293V1.5a.5.5 0 0 0-1 0v8.793L5.354 8.146a.5.5 0 1 0-.708.708l3 3z')
                        with a.div(klass='summary-container'):
                            a.button(klass='ui-button stacked', onclick='showQMAPopup()', _t='QMA Summary')
                            a.button(klass='ui-button stacked', onclick='showCMAPopup()', _t='CMA Summary')
    with a.script():
        a('window.addEventListener("DOMContentLoaded", (event) => {\n        document.getElementById("next_student_form").addEventListener("submit", function(event) {\n            event.preventDefault();\n            submitForm("next_student_form", "/next_student_endpoint");\n        });\n\n        document.getElementById("change_student_form").addEventListener("submit", function(event) {\n            event.preventDefault();\n            submitForm("change_student_form", "/change_student_endpoint");\n        });\n\n        document.getElementById("prev_student_form").addEventListener("submit", function(event) {\n            event.preventDefault();\n            submitForm("prev_student_form", "/prev_student_endpoint");\n        });\n\n    });')

    with open('templates/airFile.html', 'wb') as f:
        f.write(bytes(a))


# Takes the generated and saved metrics as parameters to generate the original html
# cur_files: list of file names for the current user
# student_info: list of tuples holding student id, name, and submission_id
# assignment_info: dict holding assignment name, due date, section title
# report_metrics: Think about it
def air_file(files, student_info, assignment_info, report_metrics, file_stu):
    # build a list of students from the student_info
    i = 0
    for student in student_info:
        file_names = []
        # attach the files to the first student
        j = 0
        for file in file_stu[student[0]]:
            # read the file
            path = 'TestAssignmentFiles/' + file[0]
            cur_file = open(path, "r")

            code = cur_file.read()
            file_scores = []
            file_complex = []

            file_complex.append(report_metrics[file[0]]['CC'])
            file_complex.append(100)
            file_complex.append(report_metrics[file[0]]['WMC'])
            file_complex.append(int(round(report_metrics[file[0]]['ABC'], 0)))
            file_scores.append(file_complex)

            file_coup_metric =[]
            file_coup_metric.append(report_metrics[file[0]]['COF'])
            file_coup_metric.append(70)
            file_scores.append(file_coup_metric)

            file_coh_metric = [report_metrics[file[0]]['DIT'], report_metrics[file[0]]['MHF'], report_metrics[file[0]]['AHF']]
            file_scores.append(file_coh_metric)

            file_name_metric = [100, 100, 100]
            file_scores.append(file_name_metric)

            file_general = [report_metrics[file[0]]['CP'], report_metrics[file[0]]['TC']]
            file_scores.append(file_general)

            print(file_scores)
            file_names.append(create_file(code, file[0], j, file_scores, file[1]))
            j = j + 1

        print(file_names)
        sub = create_submission(assignment_info["due_date"], file_names)
        this_stu = create_student(student[1], i, sub)

        student_list.append(this_stu)
        i = i+1

    a = go_here(0, 0)



if __name__ == '__main__':
    print("g")
