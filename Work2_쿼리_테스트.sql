-- ============================================================
-- Work2 - 조인 쿼리 자동 테스트 스크립트
-- 실행방법: sqlplus scott/tiger@localhost:1521/XEPDB1 @Work2_쿼리_테스트.sql
-- ============================================================

SET ECHO ON
SET FEEDBACK ON
SET SERVEROUTPUT ON
WHENEVER SQLERROR CONTINUE

-- ============================================================
-- 테스트 시작
-- ============================================================
PROMPT ============================================================
PROMPT Work2 조인 쿼리 테스트 시작
PROMPT ============================================================

-- ============================================================
-- 1. EQUI JOIN 테스트
-- ============================================================
PROMPT
PROMPT [1-1] 기본 EQUI JOIN
SELECT * FROM EMP, DEPT
WHERE EMP.DEPTNO = DEPT.DEPTNO;

PROMPT
PROMPT [1-2] 테이블 별칭 사용
SELECT * FROM EMP e, DEPT d
WHERE e.DEPTNO = d.DEPTNO;

PROMPT
PROMPT [1-3] 특정 컬럼만 조회
SELECT e.EMPNO, e.ENAME, e.SAL, d.DEPTNO
FROM EMP e, DEPT d
WHERE e.DEPTNO = d.DEPTNO;


-- ============================================================
-- 2. INNER JOIN 테스트
-- ============================================================
PROMPT
PROMPT [2-1] 기본 INNER JOIN
SELECT e.EMPNO, e.ENAME, e.SAL, d.DEPTNO
FROM EMP e
INNER JOIN DEPT d
  ON e.DEPTNO = d.DEPTNO;


-- ============================================================
-- 3. INTERSECT 테스트
-- ============================================================
PROMPT
PROMPT [3-1] INTERSECT (교집합)
SELECT DEPTNO FROM EMP
INTERSECT
SELECT DEPTNO FROM DEPT;


-- ============================================================
-- 4. OUTER JOIN 테스트
-- ============================================================
PROMPT
PROMPT [4-1] LEFT OUTER JOIN
SELECT * FROM EMP e
LEFT OUTER JOIN DEPT d
  ON e.DEPTNO = d.DEPTNO;

PROMPT
PROMPT [4-2] RIGHT OUTER JOIN
SELECT * FROM EMP e
RIGHT OUTER JOIN DEPT d
  ON e.DEPTNO = d.DEPTNO;


-- ============================================================
-- 5. CROSS JOIN 테스트
-- ============================================================
PROMPT
PROMPT [5-1] CROSS JOIN
SELECT COUNT(*) AS TOTAL_ROWS FROM EMP CROSS JOIN DEPT;


-- ============================================================
-- 6. UNION / UNION ALL 테스트
-- ============================================================
PROMPT
PROMPT [6-1] UNION (중복 제거)
SELECT COUNT(*) AS UNION_COUNT FROM (
  SELECT * FROM EMP
  UNION
  SELECT * FROM EMP
);

PROMPT
PROMPT [6-2] UNION ALL (중복 포함)
SELECT COUNT(*) AS UNION_ALL_COUNT FROM (
  SELECT * FROM EMP
  UNION ALL
  SELECT * FROM EMP
);


-- ============================================================
-- 7. MINUS 테스트
-- ============================================================
PROMPT
PROMPT [7-1] MINUS (차집합)
SELECT DEPTNO FROM DEPT
MINUS
SELECT DEPTNO FROM EMP;


-- ============================================================
-- 8. CONNECT BY 테스트 (NEXTEMP 테이블 필요)
-- ============================================================
PROMPT
PROMPT [8-1] CONNECT BY 테스트 (NEXTEMP 테이블 존재 여부 확인)

-- NEXTEMP 테이블이 있는지 확인
DECLARE
  v_count NUMBER;
BEGIN
  SELECT COUNT(*) INTO v_count
  FROM user_tables
  WHERE table_name = 'NEXTEMP';

  IF v_count = 0 THEN
    DBMS_OUTPUT.PUT_LINE('NEXTEMP 테이블이 존재하지 않습니다. CONNECT BY 테스트를 건너뜁니다.');
  ELSE
    DBMS_OUTPUT.PUT_LINE('NEXTEMP 테이블이 존재합니다. CONNECT BY 테스트를 수행합니다.');
  END IF;
END;
/

-- NEXTEMP가 있으면 실행 (없으면 에러 발생하지만 WHENEVER SQLERROR CONTINUE로 계속 진행)
PROMPT
PROMPT [8-2] CONNECT BY - 최대 레벨
SELECT MAX(LEVEL) AS MAX_LEVEL
FROM NEXTEMP
START WITH MGR IS NULL
CONNECT BY PRIOR EMPNO = MGR;

PROMPT
PROMPT [8-3] CONNECT BY - 계층 구조
SELECT LEVEL, EMPNO, MGR
FROM NEXTEMP
START WITH MGR IS NULL
CONNECT BY PRIOR EMPNO = MGR;


-- ============================================================
-- 테스트 완료
-- ============================================================
PROMPT
PROMPT ============================================================
PROMPT Work2 조인 쿼리 테스트 완료
PROMPT ============================================================
PROMPT
PROMPT 오류가 발생한 쿼리가 있다면 위 결과를 확인하세요.
PROMPT NEXTEMP 테이블이 없어서 발생한 오류는 무시해도 됩니다.
PROMPT
