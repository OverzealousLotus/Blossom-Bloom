// Control Flow is the most necessary part of a programming language.
// It allows us to control what occurs in our program, when, and why.

fn main() {
    // <===| If |===>
    // One of the most basic, "if" asks whether an evaluation is true or not.

    let mut crab: &str = "Jay";

    if crab == "Jay"{
        println!("I have a crab named Jay!");
    }
    // If we change the crab's name, this evaluation will no longer run.
    // However, we can have a fallback statement, "else" if our statement is not true.
    crab = "Veronica";

    if crab == "Jay" {
        println!("I have a crab named Jay!");
    } else {
        println!("I have a crab, their name is {crab}");
    }

    // Usually, we won't be asking one question, but many. For this, "else if" exists.
    // "else if" says if the previous statement evaluated to false, then ask if this statement is true.

    if crab == "Jay" {
        println!("I have a crab named Jay!");
    } else if crab == "Veronica" {
        println!("I have a crab, her name is Veronica.");
    } else {
        println!("I have a crab, their name is {crab}!");
    }

    // BUT! There is a better way! One I prefer in both Python, Java, and Rust!
    // The "match" keyword, allows us to match instances of a value from a variable.

    crab = "Garnet";
    match crab {
        "Jay" => println!("I have a crab named Jay!"),

        "Veronica" => println!("I have a crab, her name is Veronica."),

        "Garnet" => println!("I have a crab, their name is Garnet."),

        // "_" is a default, similar to "else" in "if" blocks.
        _ => println!("I have a crab, their name is {crab}!")
    }

    // <===| Loops |===>
    // Most of the time, we don't want our program to run once. 
    // This is where loops come in. The most basic type in Rust is "loop"
    let mut counter: u8 = 3;
    loop {
        if counter == 0 { break } // The "break" keyword will stop the loop.
        println!("My crab's name is {crab}!");
        counter -= 1;
    }

    // Loops are rather generic by themselves, so Rust has labels we can add to them.
    // They are useful for breaking the parent loop to a nested loop.
    counter = 3;
    'jail: loop {
        loop {
            // This loop is not broken, but its parent is.
            if counter == 0 { println!("I broke out!"); break 'jail; }
            println!("I'm gonna break out!");
            counter -= 1;
        }
        // This is unreachable.
    }

    // <| While |>
    // While Loops are loops which ask if a statement is still true before execution.
    // For example, let's loop "while" our counter is above zero.
    counter = 5;
    while counter != 0 {
        counter -= 1
    }
    println!("While Loop finished!");

    // <| For |>
    // Lastly, a more important loop than most others: "for"
    // These loops can go through a variable's various items.
    // If we wanted to fetch some proxies and toss them into a Vec<T>, then we would use a For Loop.

    let food: Vec<&str> = vec!("Pizza", "Chicken", "Butternut");

    for item in food {
        if item == "Pizza" { continue } // The "continue" keyword skips the next iteration of any loop.
        println!("{}", item);
    }
}