import java.util.Scanner;
import java.util.Stack;

public class VPS_9012{
	
	public static String checkVps(String ps){
		if(ps.length()%2==1 || ps.length()==0){
			return "NO";
		}
		
		Stack st = new Stack<String>();
		for(int i=0; i<ps.length(); i++){
			if(ps.charAt(i)=='('){
				st.push(ps.charAt(i));
			}
			else if(ps.charAt(i)==')'){
				if(st.size()==0){
					return "NO";
				}
				else if(st.size()>0){
					st.pop();
				}
			}
		}
		
		if(st.size()==0){
			return "YES";
		}
		else if(st.size()>0){
			return "NO";
		}
		return "?";
		
		
	}
		
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		for(int i=0; i<n; i++){
			String ps = scan.next();
			System.out.println(checkVps(ps));
		}
		
				
	}
}