# Werkzeug Tutorial

I don't understand how webservers and whatnot work, I want to understanding web application networking. I am learning.

###Learning Points



* I struggled with the environ param passed in for a while, stuck some breakpoints in it and ran it through debug, then output a print with the information, but I couldn't work out where it was coming from and how it was autopopulating. After then running it through cProfile and visualising a few varying runtimes (all of which returned different graphs, which is super interesting in itself) I reread something from the WSGI wikipedia page, so environ is obviously environment based and has to do with vars, it is effectively a config dict passed in. So as WSGI is thr Web Server Gateway Interface, it is obviously a layer that facilitates communication. This communication occurs between the Server side and Application side. Server being your Apache or Nginx and application being your script. The server (in this instance, my host computer) invokes the code, and as it invokes, the application side (script) obviously calls a function that populates the environ with host specific information. This would obviously differ from host to host.The most interesting part of all this is that it does this for each item being displayed back, so for each resource, it will respond with a slightly unique environ dict, for example: favicon.ico returns different information than the root / destination.

* Another interesting item was the way that it profiled under cProfile, I hadn't previously picked up on it simply because I wasn't really implementing much or dissecting the results. But basically what happened was that I wondered what the exec path looked like for the application server. So I ran the profiler, got a graph back, and had a look, but then as I was looking for flags to alter colours with. I ran it again, but this time, the exec path was totally different. I then started experimenting, running it then turning it off half a second later, and then running the server, spamming refresh then outputting a totally different exec path. Really interesting how it results.  
