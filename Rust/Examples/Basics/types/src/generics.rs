// Sometimes, we do not want one, or two types inputted into a function.
// This is where Generic Types in Rust come in. They allow us to expect ANY type.

// <===| Generics in Functions |===>

// To define a Generic Type in a function, we must wrap them in <> after our function name.
// Usually, Generic Types are labeled as "T" or "U" when two are present.
// However, I'll be using the NATO Phonetic Alphabet.
fn largest<Tango: PartialOrd + Copy>(list: Vec<Tango>) -> Tango {
    // "PartialOrd" and "Copy" are Traits applied to our Generic Type.
    // Think of them as restrictions to "Tango"
    // Without them, "Tango" could be anything, which is not good.
    let mut largest =  list[0];

    for item in list {
        if item > largest {
            largest = item;
        }
    }

    return largest
}

// <===| Generics in Structs |===>

// Alternatively, Generic Types can be used in Structs.
// Similar syntax is used with Structs when applying Generic Types.
struct Point<Tango, Uniform> {
    xanther: Tango,
    yankee: Uniform
}


fn main() {
    // Our function should now search through provided Vectors to find the largest number.
    println!("The largest number of our Vector is: {}", largest(vec!(10, 20, 60, 100)));

    // Time to initalize our Struct.

    let coordinates = Point  { xanther: 3, yankee: 10.8 };
    println!("The coordinates to your base are x:{}, y:{}!", coordinates.xanther, coordinates.yankee);
}