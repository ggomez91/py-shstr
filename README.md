# py-shstr
Python module that allows  shell-like string interpolation

While learning Perl I got convinced Python was far superior in most aspects but Perl had strign interpolations just like bash. Of course I wanted this on Python so I did this little module to allows such thing. 

The idea is simple: Call the shstr function passing your base string and the functino will replace the $KEYs with the nearest variable in scope. 

Ultimately I want this to work with any level of nested-locals but currently it only handles one level up. 

Ideally all bash $-expansions should work. 

TODO: Nestes scopes
TODO: all shell expansions

