# Java Compile Example
This project provides a simple example of using Docker containers to build and run a Java application without installing Java.
I totally ripped this off of another example, and I'm pretty sure they stole it before I did. I don't plan to make any money off of this thing, but if you do I'd like a share!

## Compile Java Class

When building a Java application we need a Java Development Kit (JDK). We can use an 
existing Docker image with a JDK in it to build our class.

On linux use:
```
docker run -it -v $(pwd):/build openjdk:8u131-jdk-alpine javac /build/HelloWorld.java
```

On GitBash (if your command prompt includes MINGW) use:
```
MSYS_NO_PATHCONV=1 docker run -it -v $(pwd):/buid openjdk:8u131-jdk-apline javac /build/HelloWorld.java
```

## Build Docker Container Image

We can then take our Java class file (aka our build artifact) and bundle it into a 
container image.

```
docker build -t hello-java .
```

## Run Container

Once we have a compiled Java class we can simply execute it with a Java Runtime Environment (JRE).

```
docker run -it --rm=true hello-java
```