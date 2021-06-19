package lec5;

import java.util.Arrays;
import java.util.Scanner;

public class Lec5{
    
    static char letters[] = "abcdefghijklmnopqrstuvwxyz".toCharArray();
    
    static String char2num(char c){
        int index = Arrays.binarySearch(letters, c) + 1;
        return index < 10 ? "0" + index : Integer.toString(index);
    }
    
    static String str2num(String str){
        String nums[] = new String[str.length()];
        for (int i=0; i < str.length(); i++){
            nums[i] = char2num(str.charAt(i));
        }
        return String.join("", nums);
    }
    
    public static void main(String args[]){
        System.out.println(str2num("victory"));
    
    }
}