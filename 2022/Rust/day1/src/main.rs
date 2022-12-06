use std::fs;
fn part_one() -> i32 {
    let path: String = "in.txt".to_string();
    let contents = fs::read_to_string(path).expect("Should have been able to read file");
    let lines = contents.split("\r\n");
    let mut totals: Vec<i32> = vec![];
    let mut total: i32 = 0;
    for i in lines {
        if i == "" {
            totals.push(total);
            total = 0;
            continue;
        }
        total += i.parse::<i32>().unwrap();
    }
    totals.push(total);
    totals.sort();
    totals.reverse();
    totals[0]
}
fn part_two() -> i32 {
    let path: String = "in.txt".to_string();
    let contents = fs::read_to_string(path).expect("Should have been able to read file");
    let lines = contents.split("\r\n");
    let mut totals: Vec<i32> = vec![];
    let mut total: i32 = 0;
    for i in lines {
        if i == "" {
            totals.push(total);
            total = 0;
            continue;
        }
        total += i.parse::<i32>().unwrap();
    }
    totals.push(total);
    totals.sort();
    totals.reverse();
    totals[0] + totals[1] + totals[2]
}
fn main() {
    println!("Part 1 result: {}", part_one());
    println!("Part 2 result: {}", part_two());
}
