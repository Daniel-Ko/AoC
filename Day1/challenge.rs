use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    partA();
    partB();
}

fn partA() {
    let mut num_depth_incr = 0;
    let mut prev_depth = -1;
    if let Ok(lines) = read_lines("./input.txt") {
        for line in lines {
            if let Ok(depth) = line {
                let depth: i32 = depth.trim().parse().expect("num");
            
            if prev_depth != -1 && depth > prev_depth {
                    num_depth_incr += 1;
                }
                prev_depth = depth;
            }
        }
        println!("{}", num_depth_incr); // Account for the first number from -1 
    }
}

fn partB() {
    let mut num_depth_incr = 0;
    let mut prev_window = [-1, -1, -1];

    if let Ok(lines) = read_lines("./input.txt") {
        for line in lines {
            if let Ok(depth) = line {
                let depth: i32 = depth.trim().parse().expect("num");
                let curr_window = [prev_window[1], prev_window[2], depth];

                let prev_sum:i32 = prev_window.iter().sum();
                let curr_sum:i32 = curr_window.iter().sum();
                
                if ! prev_window.contains(&-1) &&  curr_sum > prev_sum {
                    num_depth_incr += 1;
                }
                prev_window = curr_window;
            }
        }
        println!("{}", num_depth_incr); // Account for the first number from -1 
    }
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
