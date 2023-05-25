package practice;

import java.util.Scanner;

public class NQueens {

	public static void main(String[] args) 
	{
		System.out.print("Enter size of board : ");
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        boolean[][] board = new boolean[n][n];
        // ArrayList<ArrayList<Integer>> ans = queensRet(board,0);
        // bubbleSort(ans);

        int NoOfCombinations = queens(board,0);
        System.out.print("Number of Combinations are : ");
        System.out.println(NoOfCombinations);
	}
	static int queens(boolean[][] board,int row){
        if(row == board.length){
            display(board);
            System.out.println();
            return 1;
        }
        // placing the queen and checking for every row and column
        int count=0;
        for(int col=0;col<board.length;col++){
            if(isSafe(board,row,col)){
                board[row][col] = true;
                count+=queens(board,row+1);
                board[row][col] = false;//backtrack
            }
        }
        return count;
    } 
    
    static boolean isSafe(boolean[][] board,int row,int col){
        // checking vertically
        for(int i=0;i<row;i++){
            if(board[i][col]){
                return false;
            }
        }
        // left diagonal
        int leftmax = Math.min(row,col);
        for(int i=1;i<=leftmax;i++){
            if(board[row-i][col-i]){
                return false;
            }
        }
        // right diagonal
        int rightmax = Math.min(row,board.length - col - 1);
        for(int i=1;i<=rightmax;i++){
            if(board[row-i][col+i]){
                return false;
            }
        }
        // if all of the above returns nothing means place is safe so return true finally
        return true;
    }
    //display function
    static void display(boolean[][]board){
        
        for(boolean[] row : board){
            for(boolean element: row){
                if(element){
                    System.out.print("Q ");
                }
                else{
                    System.out.print("X ");
                }
            }
            System.out.println();
        }
    }

}


