// In Rust, we can define variables to use throughout our program.
// Or... For a moment if you wish.

const CHICKEN: &str = "uwu";

fn main() {
    // There are three types of variables in Rust:
    // let: Standard, immutable by default.
    // const: Constant, often immutable variable.
    // static: Longest lifetime, nearly always immutable.

    println!("{CHICKEN}");
    let gold: u8 = 100;

    println!("John: I have {gold} gold pieces!");

    // If we want to define a mutable variable, we use the "mut" keyword.

    let mut silver: u8 = 100;

    println!("Mariot: Cool! I have {silver} silver pieces!");

    silver -= 50; // Here, we subtract fifty from "silver"

    println!("Thief: Mine now!");
    println!("Mariot: Nooo! Now I only have {silver} silver pieces...");

    // What if we don't want our value to change?

    const BRONZE: u8 = 25; // Constants must be uppercase.\

    println!("Garnet: You're one to talk. I only have {BRONZE} bronze pieces.");
    println!("Mariot: I guess you're right...");

    silver /= 2;

    println!("Mariot: Wait... I miscounted! I have {silver} silver!");

    // Lastly, we have a method I do not have much experience in.
    // However, "static" is similar to "const", except it has a much longer lifetime?

    static BITS: u8 = 16; // The uppercase naming style applies to statics too.

    println!("At least none of you have {BITS} bits...");
}
