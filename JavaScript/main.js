/* root-algorithmic-analysis in JS 
   Author: seojun0602
*/

/**
  * 절댓값
  * @this {number}
  * @return {number} - 절댓값
  */
Number.prototype.abs=function(){
  return ((n=this.valueOf())>=0)?(n):(-n);
}

/**
  * 최대공약수 구하기
  * @this {number[]} - 수들을 담은 배열
  * @return {number} - 최대공약수 (절댓값)
  */
Array.prototype.gcd=function(){
  const gcd = (a, b) => {
    while(b!==0) [a, b] = [b, a % b];
    return a;
  }
  return ((this.valueOf().length>0)?(this.valueOf().reduce((a,b)=>gcd(a,b))):(+[][[]])).abs();
}

/**
  * 소수를 분수화.
  * @this {number} - 소수 표현 (e.g. 0.123)
  * @return {string} - 분수 표현 (e.g. 123/1000)
  * @throws {Error} 유효하지 않은 소수 형식일 경우
  */
Number.prototype.toFrac=function(){
  let n=this.valueOf().toString(), 
      frac = n.split("."), sign=(n>=0)?(1):(-1);
      if(!isNaN(frac)) return frac.push(1)&&frac.join("/");
    (frac.length>1)?((dec=+frac[1])&&(deno=(+(1+"0".repeat(frac[1].length)))))&&(int=+frac[0]):(eval("throw \"Invalid decimal number format\\nExpected: A decimal number like 0.1234\""));
    let nume = sign*(int.abs()*deno+dec),
    fracs = [nume,deno], gcd=fracs.gcd()||1;
    return fracs.map(e => {
        return e/gcd;
    }).join("/");
}

/**
  * Fast-Exponentiation-Algorithm (지수가 정수일때)
  * Newton–Raphson method (지수가 정수가 아닐때)
  * Reference: https://me2.kr/JLOQT
  * @this {number} - 밑
  * @param {number} - power 지수
  * @return {number}
  */
Number.prototype.pow=function(power){ 
    let f=1, b = this.valueOf();
    if(power.abs()<1){
      if(power === 0) return 1;
      let p = (1/(power)).abs(), xz=b;
      re2lation = (x) => { return (x.pow(p)-b)/(p*(x.pow(p-1))) };
      do { xz-=(re2lation(xz)); }  
      while(re2lation(xz)>1e-15)
      return (power>0)?(xz):(1/xz);
    }
    while (parseInt(power.abs()) > 0){
       if(parseInt(power.abs()) % 2 === 1) f *= b;
       b *= b;
       power/=2;
    }
    return (power>0)?(f):(1/f);
}

/**
  * Factorial
  * Source: cafe.naver.com/nameyee/38284
  * @param {number}
  * @return {number}
  */
Number.prototype.fac = function(){
  let num = this.valueOf(), result = 1;
  if(num === 0 || num === 1){ return 1; }
   for(let i=1;i<=num;i++){result*=i}
   return ((result==1)?(NaN):result);
}

π = (() => {
/** PI
  * Source: cafe.naver.com/nameyee/38284
  * @return {number} - PI
  */
  let stand = (2*((2).pow(0.5))/9801), sum = 0, i=0;
   recurr = (k) => {
     return ((4 * k).fac() * (1103 + 26390 * k))/(((k).fac().pow(4)) * (396).pow(4 * k));
   };
    do { sum += recurr(i); i++; }
    while(recurr(i)>0);
    return 1/(stand*sum);
})();

/**
  * 테일러 급수를 통한 사인함수 계산
  * @param {number} r - 라디안
  * @return {number} 함수값
  */
function sints(r){
  let ft=r, sign=function(n) { return (((n-3)%4)===0)?(-1):(1)}, gt=function(n){ return sign(n)*(r.pow(n)/n.fac())};
  for(let i=3;i<100;i+=2){
  ft += gt(i);
  }
  return +(ft.toFixed(10));
}

/**
  * 테일러 급수를 통한 코사인함수 계산
  * @param {number} r - 라디안
  * @return {number} 함수값
  */
function costs(r){
  let ft=1, sign=function(n) { return (((n-2)%4)===0)?(-1):(1)}, gt=function(n){ return sign(n)*(r.pow(n)/n.fac())};
  for(let i=2;i<100;i+=2){
  ft += gt(i);
  }
  return +(ft.toFixed(10));
}

/**
  * 테일러 급수를 통한 아크탄젠트 함수 계산
  * @param {number} x - input
  * @return {number} 함수값
  */
function atan(x){
  let ft=x, sign=function(n) { return (((n-3)%4)===0)?(-1):(1)}, gt=function(n){ return sign(n)*(x.pow(n)/n)};
  if (x > 1) return (π/2)-atan(1/x);
  if (x < -1) return -(π/2)-atan(1/x);
  for(let i=3;i<100;i+=2){
  ft += gt(i);
  }
  return +(ft.toFixed(10));
}

 /**
   * 복소수의 극형식을 이용한 거듭제곱근 계산
   * @param {string} cplxNum - 피근수(복소수 형식)
   * @param {number} index - 근지수
   * @return {string[]} 복소수 형식의 결과값을 담은 배열
  */
function rootCplx(cplxNum, index, mxdecp=3, frac=false){
  let regex = /^([+-]?(?:\d+\/\d+|\d+(?:\.\d+)?))([+-]?(?:\d+\/\d+|\d+(?:\.\d+)?)i)?$|^([+-]?(?:\d+\/\d+|\d+(?:\.\d+)?)i)([+-]?(?:\d+\/\d+|\d+(?:\.\d+)?))?$/, p = (cplxNum=cplxNum.toString()).match(regex);
  if(!regex.test(cplxNum)) throw new Error("Invalid complex number format.\n\
Expected formats: a+bi, a-bi, bi, -bi, a, where a and b are integers.");
  let r = parseInt(p[1] || p[4])||0, 
      i = parseInt(p[2] || p[3])||0,
      γ = (r.pow(2)+i.pow(2)).pow(1/2),
      θ = atan(i/r), result = [];
      for(let k=0;k<index;k++){
        let φ = (θ+(2*k*π))/index;
        coe = γ.pow(1/index),
        decp = parseInt(1+"0".repeat((mxdecp>7)?(mxdecp):mxdecp));       result.push([Math.round(coe*costs(φ)*decp)/decp, Math.round(coe*sints(φ)*decp)/decp]);
    }
    return result.map((e)=>{ return [(e[0]!=0)?(e[0]%1==0)?(e[0]):((frac)?e[0].toFrac():e[0]):(""),(e[1]>0)?("+"):(""),(e[1]!=0)?(e[1]+"𝑖"):("")].join("")});
}
