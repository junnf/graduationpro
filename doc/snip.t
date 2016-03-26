public static boolean isChineseChar(String str){
    boolean temp = false;
    Pattern p=Pattern.compile("[\u4e00-\u9fa5]");
    Matcher m=p.matcher(str);
    if(m.find()){
        temp =  true;
    }
    return temp;
}
