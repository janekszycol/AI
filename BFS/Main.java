package SztucznaInteligencja.podstawa;

import java.util.*;
import java.util.stream.Collectors;

public class BFS {

    static class Board implements Comparable<Board>{
        List<int[]> board;
        int rank;
        public Board() {
            this.board = new ArrayList<>();
            this.rank =0;
        }

        public Board(List<int[]> b) {
            this.board = new ArrayList<>(b);
        }

        public Board(List<int[]> board, int rank) {
            this.board = board;
            this.rank = rank;
        }


        @Override
        public int compareTo(Board o) {
            if(rank==o.rank) return Integer.compare(o.board.size(), board.size());
            return Integer.compare(rank,o.rank);
        }
    }



    //dla true BFS
    public static List<int[]> solver(String przelacznik, int size) {
        long millisActualTime = System.currentTimeMillis();
        if (Objects.equals(przelacznik, "h1")) {
            //BFS
            List<Board> closed = new ArrayList<>();

            //List<int[]> board = new ArrayList<>();
            //board.add(new int[]{});

            Board board = new Board();
            board.board.add(new int[]{});

            h1(board);

            //List<List<int[]>> open = new ArrayList<>();
            //open.add(board);

            PriorityQueue<Board> open=new PriorityQueue<>();
            open.add(board);

            List<int[]> tabList = new ArrayList<>();
            for (int i = 0; i < size; i++) {
                for (int j = 0; j < size; j++) {
                    tabList.add(new int[]{i, j});
                }
            }


            while (!open.isEmpty()) {

                //board = open.get(0);
                //open.remove(0);

                board = open.poll();

                if (conflict_checker(board) && size == board.board.size()) {
                    System.out.println("znalazlo");
                    for (int[] t : board.board) {
                        System.out.println(Arrays.toString(t));
                    }
                    long executionTime = System.currentTimeMillis() - millisActualTime;
                    System.out.println("Czas trwania programu: " + executionTime+ "ms.");
                    System.out.println("Dlugosc listy open: " + open.size());
                    System.out.println("Dlugosc listy closed: " + closed.size());
                    //print_board(board.board,przelacznik);
                    return board.board;
                }


                List<Board> childrens = generate_children(board.board, size, tabList);


                for (Board child : childrens) {
                    if (closed.contains(board)) continue;
                    h1(child);
                    if(!open.contains(child)) open.add(child);
                    else{
                        if(child.rank< board.rank) board.rank= board.rank+100;
                    }
                }

                closed.add(board);
            }
            System.out.println("nie znalazlo");
            long executionTime = System.currentTimeMillis() - millisActualTime;
            System.out.println("Czas trwania programu: " + executionTime+ "ms.");
            System.out.println("Dlugosc listy open: " + open.size());
            System.out.println("Dlugosc listy closed: " + closed.size());
            return new ArrayList<>();
        }

        else if (Objects.equals(przelacznik, "h2")) {
            //BFS h2
            List<Board> closed = new ArrayList<>();

            //List<int[]> board = new ArrayList<>();
            //board.add(new int[]{});

            Board board = new Board();
            board.board.add(new int[]{});

            //h2(board,size);
            //List<List<int[]>> open = new ArrayList<>();
            //open.add(board);

            PriorityQueue<Board> open=new PriorityQueue<>();
            open.add(board);

            List<int[]> tabList = new ArrayList<>();
            for (int i = 0; i < size; i++) {
                for (int j = 0; j < size; j++) {
                    tabList.add(new int[]{i, j});
                }
            }


            while (!open.isEmpty()) {

                //board = open.get(0);
                //open.remove(0);

                board = open.poll();

                if (conflict_checker(board) && size == board.board.size()) {
                    System.out.println("znalazlo");
                    for (int[] t : board.board) {
                        System.out.println(Arrays.toString(t));
                    }
                    long executionTime = System.currentTimeMillis() - millisActualTime;
                    System.out.println("Czas trwania programu: " + executionTime+ "ms.");
                    System.out.println("Dlugosc listy open: " + open.size());
                    System.out.println("Dlugosc listy closed: " + closed.size());
                    //print_board(board.board,przelacznik);
                    return board.board;
                }


                List<Board> childrens = generate_children(board.board, size, tabList);


                for (Board child : childrens) {
                    if (closed.contains(board)) continue;
                    h2(child,size);
                    if(!open.contains(child)) open.add(child);
                    else{
                        if(child.rank< board.rank) board.rank= board.rank+100;
                    }
                }

                closed.add(board);

            }
            System.out.println("nie znalazlo");
            long executionTime = System.currentTimeMillis() - millisActualTime;
            System.out.println("Czas trwania programu: " + executionTime+ "ms.");
            System.out.println("Dlugosc listy open: " + open.size());
            System.out.println("Dlugosc listy closed: " + closed.size());
            return new ArrayList<>();



        }
        else if (Objects.equals(przelacznik, "h3")) {
            //BFS h3
            List<Board> closed = new ArrayList<>();

            //List<int[]> board = new ArrayList<>();
            //board.add(new int[]{});

            Board board = new Board();
            board.board.add(new int[]{});

            //h2(board,size);
            //List<List<int[]>> open = new ArrayList<>();
            //open.add(board);

            PriorityQueue<Board> open = new PriorityQueue<>();
            open.add(board);

            List<int[]> tabList = new ArrayList<>();
            for (int i = 0; i < size; i++) {
                for (int j = 0; j < size; j++) {
                    tabList.add(new int[]{i, j});
                }
            }


            while (!open.isEmpty()) {

                //board = open.get(0);
                //open.remove(0);

                board = open.poll();

                if (conflict_checker(board) && size == board.board.size()) {
                    System.out.println("znalazlo");
                    for (int[] t : board.board) {
                        System.out.println(Arrays.toString(t));
                    }
                    long executionTime = System.currentTimeMillis() - millisActualTime;
                    System.out.println("Czas trwania programu: " + executionTime + "ms.");
                    System.out.println("Dlugosc listy open: " + open.size());
                    System.out.println("Dlugosc listy closed: " + closed.size());
                    //print_board(board.board, przelacznik);
                    return board.board;
                }


                List<Board> childrens = generate_children(board.board, size, tabList);


                for (Board child : childrens) {
                    if (closed.contains(board)) continue;
                    h3(child, size);
                    if (!open.contains(child)) open.add(child);
                    else {
                        if (child.rank < board.rank) board.rank = board.rank + 100;
                    }
                }

                closed.add(board);

            }
            System.out.println("nie znalazlo");
            long executionTime = System.currentTimeMillis() - millisActualTime;
            System.out.println("Czas trwania programu: " + executionTime + "ms.");
            System.out.println("Dlugosc listy open: " + open.size());
            System.out.println("Dlugosc listy closed: " + closed.size());
            return new ArrayList<>();
        }

        return new ArrayList<>();
    }


    public static void h1(Board b){
        if(!conflict_checker(b)){
            b.rank=b.rank+100;
        }
    }

    public static void h2(Board b,int size){
        h1(b);
        if(b.rank>=100 || b.board.size()==size) return;
        else {
            if(size%2==0){

                if (b.board.size()%2==0){
                    int[] tab=b.board.get(b.board.size()-1);
                    if (tab[0]!=(size/2)+(int)Math.floor((double)b.board.size()/2)-1) b.rank+=10;
                }
                else {
                    int[] tab=b.board.get(b.board.size()-1);
                    if (tab[0]!=(size/2)-(int)Math.floor((double)b.board.size()/2)-1) b.rank+=10;
                }

            }
            else{
                if (b.board.size()%2==0){
                    int[] tab=b.board.get(b.board.size()-1);
                    if (tab[0]!=(int)Math.ceil((double) size/2)-(int)Math.floor((double) b.board.size()/2)-1) b.rank+=10;
                }
                else {
                    int[] tab=b.board.get(b.board.size()-1);
                    if (tab[0]!=(int)Math.ceil((double) size/2)+(int)Math.floor((double) b.board.size()/2)-1) b.rank+=10;
                }

            }
        }
    }

    public static void h3(Board b,int size){
        h1(b);
        if(b.rank>=100 || b.board.size()==size) return;

        for (int i = 0; i < b.board.size()-1; i++) {
            int[] t1=b.board.get(i);
            int[] t2=b.board.get(i+1);

            if(!(t1[0]+2==t2[0]&&t1[1]+1==t2[1] || t1[0]+1==t2[0]&&t1[1]+2==t2[1])){
                b.rank+=20;
            }
        }
    }




    public static List<Board> generate_children(List<int[]> b, int size, List<int[]> tabList) {

        List<int[]> board = new ArrayList<>(b);
        List<Board> childrens = new ArrayList<>();
        if (board.size() == size) return childrens;

        List<int[]> t = new ArrayList<>(tabList);

        List<int[]> t2 = new ArrayList<>(t);

        for (int[] tab : board) {
            for (int[] tab2 : t2) {
                if (Arrays.equals(tab, tab2)) {
                    t.remove(tab2);
                }
            }
        }
        if (board.get(0).length == 0) {
            for (int[] tab : t) {
                Board list = new Board();
                list.board.add(tab);
                childrens.add(list);
            }
            return childrens;
        }

        for (int[] tab : t) {
            Board list = new Board(board);
            list.board=board;
            list.board.add(tab);
            childrens.add(new Board(list.board));
            list.board.remove(tab);
        }

        return childrens;
    }




    //zwraca true jezeli nie ma bic
    public static boolean conflict_checker(Board currList) {

        int size = currList.board.size();


        for (int i = 0; i < size; i++) {
            int[] tab1 = currList.board.get(i);
            for (int m = 0; m < size; m++) {
                int[] tab2 = currList.board.get(m);
                if (i == m) continue;
                if (tab1[0] == tab2[0] || tab1[1] == tab2[1]) {
                    return false;
                }

                for (int x = 1; x < size; x++) {
                    if ((tab1[0] == tab2[0] + x || tab1[0] == tab2[0] - x) && (tab1[1] == tab2[1] + x || tab1[1] == tab2[1] - x)) {
                        return false;
                    }
                }
            }
        }

        return true;
    }

    public static void print_board(List<int[]> board,String przelacznik) {

        if(Objects.equals(przelacznik, "h1")) {
            int licznik=0;
            for (int i = 0; i < board.size(); i++) {
                int[] tab = board.get(licznik);
                for (int j = 0; j < board.size(); j++) {

                    if (tab[0] == i && tab[1] == j) {
                        System.out.print("[X]");
                        licznik++;
                    } else System.out.print("[ ]");
                }
                System.out.println();
            }
        }
        else {


            int licznik= board.size()-1;
            for (int i = 0; i < board.size(); i++) {
                int[] tab = board.get(licznik);
                for (int j = 0; j < board.size(); j++) {

                    if (tab[0] == i && tab[1] == j) {
                        System.out.print("[X]");
                        licznik--;
                    } else System.out.print("[ ]");
                }
                System.out.println();
            }
        }

    }


    public static void main(String[] args) {

        //solver("h1", 7);
        solver("h2", 25);
        //solver("h3", 20);
        }
}