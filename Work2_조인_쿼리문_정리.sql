-- ============================================================
-- Work2 - 조인(JOIN) 쿼리문 정리
-- 출처: 조인.pptx
-- ============================================================

-- ============================================================
-- 1. EQUI JOIN (동등 조인)
-- ============================================================

-- 기본 EQUI JOIN
SELECT * FROM EMP, DEPT
WHERE EMP.DEPTNO = DEPT.DEPTNO;

-- 테이블 별칭 사용
SELECT * FROM EMP e, DEPT d
WHERE e.DEPTNO = d.DEPTNO;

-- 특정 컬럼만 조회
SELECT e.EMPNO, e.ENAME, e.SAL, d.DEPTNO
FROM EMP e, DEPT d
WHERE e.DEPTNO = d.DEPTNO;

-- WHERE 조건 추가
SELECT e.EMPNO, e.ENAME, e.SAL, d.DEPTNO
FROM EMP e, DEPT d
WHERE e.DEPTNO = d.DEPTNO
  AND e.ENAME LIKE '김%';


-- ============================================================
-- 2. INNER JOIN (ISO 표준 SQL)
-- ============================================================

-- 기본 INNER JOIN
SELECT e.EMPNO, e.ENAME, e.SAL, d.DEPTNO
FROM EMP e
INNER JOIN DEPT d
  ON e.DEPTNO = d.DEPTNO;

-- WHERE 조건 추가
SELECT e.EMPNO, e.ENAME, e.SAL, d.DEPTNO
FROM EMP e
INNER JOIN DEPT d
  ON e.DEPTNO = d.DEPTNO
 AND e.ENAME LIKE '김%';


-- ============================================================
-- 3. INTERSECT (교집합)
-- ============================================================

-- 두 테이블에서 교집합 조회
SELECT DEPTNO FROM EMP
INTERSECT
SELECT DEPTNO FROM DEPT;


-- ============================================================
-- 4. OUTER JOIN
-- ============================================================

-- LEFT OUTER JOIN (왼쪽 테이블의 모든 데이터 포함)
SELECT * FROM EMP e
LEFT OUTER JOIN DEPT d
  ON e.DEPTNO = d.DEPTNO;

-- RIGHT OUTER JOIN (오른쪽 테이블의 모든 데이터 포함)
SELECT * FROM EMP e
RIGHT OUTER JOIN DEPT d
  ON e.DEPTNO = d.DEPTNO;


-- ============================================================
-- 5. CROSS JOIN (카테시안 곱)
-- ============================================================

-- CROSS JOIN (모든 조합)
SELECT * FROM EMP
CROSS JOIN DEPT;

-- 동일한 결과 (조건 없이)
SELECT * FROM EMP, DEPT;


-- ============================================================
-- 6. UNION / UNION ALL (합집합)
-- ============================================================

-- UNION (중복 제거)
SELECT * FROM EMP
UNION
SELECT * FROM EMP;

-- UNION ALL (중복 포함)
SELECT * FROM EMP
UNION ALL
SELECT * FROM EMP;


-- ============================================================
-- 7. MINUS (차집합)
-- ============================================================

-- 차집합 조회 (DEPT에는 있고 EMP에는 없는 DEPTNO)
SELECT DEPTNO FROM DEPT
MINUS
SELECT DEPTNO FROM EMP;


-- ============================================================
-- 8. CONNECT BY (계층형 쿼리)
-- ============================================================

-- 최대 레벨 조회
SELECT MAX(LEVEL)
FROM NEXTEMP
START WITH MGR IS NULL
CONNECT BY PRIOR EMPNO = MGR;

-- 계층 구조 조회
-- 참고: NEXTEMP 테이블 구조에 따라 컬럼명 변경 필요 (EMPNAME 또는 ENAME)
SELECT LEVEL, EMPNO, MGR, ENAME
FROM NEXTEMP
START WITH MGR IS NULL
CONNECT BY PRIOR EMPNO = MGR;

-- LPAD 함수로 계층 표현
SELECT LEVEL,
       LPAD(' ', 4*(LEVEL-1)) || EMPNO AS EMPNO,
       MGR,
       CONNECT_BY_ISLEAF
FROM NEXTEMP
START WITH MGR IS NULL
CONNECT BY PRIOR EMPNO = MGR;

-- 역방향 계층형 쿼리 (자식에서 부모로)
SELECT LEVEL,
       LPAD(' ', 4*(LEVEL-1)) || EMPNO AS EMPNO,
       MGR,
       CONNECT_BY_ISLEAF
FROM NEXTEMP
START WITH EMPNO = 1008
CONNECT BY PRIOR MGR = EMPNO;


-- ============================================================
-- 참고사항
-- ============================================================
-- EQUI JOIN = INNER JOIN (같은 개념)
-- OUTER JOIN: LEFT, RIGHT, FULL
-- CROSS JOIN: 카테시안 곱 (모든 조합)
-- UNION: 중복 제거, UNION ALL: 중복 포함
-- MINUS: Oracle 전용 (PostgreSQL에서는 EXCEPT)
-- CONNECT BY: Oracle 계층형 쿼리 전용
-- ============================================================
