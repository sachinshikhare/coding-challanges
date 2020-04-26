package main.java;

import java.util.function.Consumer;

public class JavaTester {
    public static void main(String[] args) {

        System.out.println(6 &2 );

        System.out.println("Hello World!");

        Consumer<String> consumer = System.out::println;

        consumer.accept("sachin");
        consumer.accept("shikhare");

        System.out.println(3/4);


    }
}
