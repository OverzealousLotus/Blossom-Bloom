// Mathematics is extremely important for anything to do with Programming.
// Even if it's the simplest of operations, it will get you far. No need for Calculus.
// Bear in mind, a u8 cannot be added together with an i8, or a u16 with a u32.
// Both variables must be of the same type.

fn main() {
    let mut dummy: u16 = 1;
    let mut dud: u16 = 1;
    println!("dummy: {dummy} | dud: {dud}");

    // Addition

    let mut dunder: u16 = dummy + dud;
    println!("dunder: {dunder}");

    // Addition Assignment
    dummy += dud;
    dud += dummy;
    println!("dud: {dud} | dummy: {dummy}");

    // Subtraction
    let mut matted: u16 = dummy - dud;
    println!("matted: {matted}");

    // Subtraction Assignment
    dunder -= dud;
    println!("dummy: {dummy}");

    // Multiplication
    dunder = dunder * 4;
    println!("dunder: {dunder}");

    // Multiplication Assignment
    dud *= 8;
    println!("dud: {dud}");

    // Division
    dud = dud / 2;
    println!("dud: {dud}");

    // Division Assignment
    matted /= matted;
    println!("matted: {matted}");

    // Modulus ( Division but return remainder )
    dud = dud % 3;
    println!("dud: {dud}");

    // Modulus Assignment
    dunder %= 5;
    println!("dunder: {dunder}");
}
