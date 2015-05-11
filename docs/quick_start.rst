Requirements
============

The requirements necessary to use this Django Project Boilerplate are:

- **python3** and **pip3**
- **virtualenv and virtualenvwrapper**
- **Firefox** (to use Selenium's Webdriver in functional Tests)
- **GNU gettext** (to use Internationalization)

If you don't have the first two requirements, you may find this
post useful: |python_install|.

.. |python_install| raw:: html

    <a href="http://www.marinamele.com/2014/07/install-python3-on-mac-os-x-and-use-virtualenv-and-virtualenvwrapper.html" target="_blank">Install Python 3 on Mac OS X and use virtualenv and virtualenvwrapper</a>

You can download Firefox from the official web page: |firefox_web|.

.. |firefox_web| raw:: html

    <a href="https://www.mozilla.org" target="_blank">Firefox</a>

And if you don't have GNU gettext, check this |taskbuster_section|.

.. |taskbuster_section| raw:: html

    <a href="http://marinamele.com/taskbuster-django-tutorial/internationalization-localization-languages-time-zones" target="_blank">TaskBuster tutorial section</a>


**Ready!?** Continue to the :doc:`quick_start`!

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
Quick Start Guide
=================


Download TaskBuster Django Project Boilerplate
----------------------------------------------

First, you need to download the BoilerPlate from GitHub.


Secret Django Key
-----------------

This boilerplate has the **DJANGO_KEY** setting variable hidden.

You can generate your DJANGO_KEY |django_key|.

.. |django_key| raw:: html

    <a href="http://www.miniwebtool.com/django-secret-key-generator"
    target="_blank">here</a>


Project Name
------------

This project is named *TaskBuster*, so if you are using this
Boilerplate to create your own project, you'll have to change
the name in a few places:

 - *taskbuster_project* **folder** (your top project container)
 - *taskbuster_project/taskbuster* **folder** (your project name)
 - virtual environment names: **tb_dev** and **tb_test** (name them whatever you want)
 - in virtual environments **postactivate** files (see section below), you have to change **taskbuster.settings.development** for your **projectname.settings.development**. Same works for the testing environment.


Virtual environments and Settings Files
---------------------------------------

First, you must know your Python 3 path::

    $ which python3

which is something similar to /usr/local/bin/python3.

Next, create a Development virtual environment with Python 3 installed::

    $ mkvirtualenv --python=/usr/local/bin/python3 tb_dev

where you might need to change it with your python path.

Go to the virtual enviornment folder with::

    $ cd $VIRTUAL_ENV/bin

and edit the postactivate file.:

    $ vi postactivate

You must add the lines: ::

    export DJANGO_SETTINGS_MODULE="taskbuster.settings.development"
    export SECRET_KEY="your_secret_django_key"

with your project name and your own secret key.

Next, edit the **predeactivate** file and add the line::

    unset SECRET_KEY

Repeat the last steps for your testing environment::

    $ mkvirtualenv --python=/usr/local/bin/python3 tb_test
    $ cd $VIRTUAL_ENV/bin
    $ vi postactivate

where you have to add the lines::

    export DJANGO_SETTINGS_MODULE="taskbuster.settings.testing"
    export SECRET_KEY="your_secret_django_key"

and in the predeactivate file::

    unset SECRET_KEY

Next, install the packages in each environment::

    $ workon tb_dev
    $ pip install -r requirements/development.txt
    $ workon tb_test
    $ pip install -r requirements/testing.txt



Internationalization and Localization
-------------------------------------

Settings
********

The default language for this Project is **English**, and we use internatinalization to translate the text into Catalan.

If you want to change the translation language, or include a new one, you just need to modify the **LANGUAGES** variable in the file *settings/base.py*. The language codes that define each language can be found |codes_link|.

.. |codes_link| raw:: html

    <a href="http://msdn.microsoft.com/en-us/library/ms533052(v=vs.85).aspx" target="_blank">here</a>

For example, if you want to use German you should include::

    LANGUAGES = (
        ...
        'de', _("German"),
        ...
    )

You can also specify a dialect, like Luxembourg's German with::

    LANGUAGES = (
        ...
        'de-lu', _("Luxemburg's German"),
        ...
    )

Note: the name inside the translation function _("") is the language name in the default language (English).

More information on the |internationalization_post|.

.. |internationalization_post| raw:: html

    <a href="http://marinamele.com/taskbuster-django-tutorial/internationalization-localization-languages-time-zones" target="_blank">TaskBuster post</a>


Translation
***********

Go to the terminal, inside the taskbuster_project folder and create the files to translate with::

    $ python manage.py makemessages -l ca

change the language "ca" for your selected language.

Next, go to the locale folder of your language::

    $ cd taskbuster/locale/ca/LC_MESSAGES

where taskbuster is your project folder. You have to edit the file *django.po* and translate the strings. You can find more information about how to translate the strings |translation_strings_post|.

.. |translation_strings_post| raw:: html

    <a href="http://marinamele.com/taskbuster-django-tutorial/internationalization-localization-languages-time-zones#inter-translation" target="_blank">here</a>

Once the translation is done, compile your messages with::

    $ python manage.py compilemessages -l ca



Tests
*****

We need to update the languages in our Tests to make sure the translation works correclty. Open the file *functional_tests/test_all_users.py*:

- in **test_internationalization**, update your languages with the translation of title text, here "Welcome to TaskBuster!"
- in **test_localization**, update your languages.



Useful commands
---------------

A list of all the commands used to run this template::

    $ workon tb_dev
    $ workon tb_test

    $ python manage.py makemessages -l ca
    $ python manage.py compilemessages -l ca