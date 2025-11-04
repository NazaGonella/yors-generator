let s:script_dir = expand('<sfile>:p:h')
augroup markdown_shortcuts
  autocmd!
  autocmd FileType markdown inoremap <buffer> <C-b> ****<Left><Left>
  autocmd FileType markdown inoremap <buffer> <C-i> **<Left>
  autocmd FileType markdown inoremap <buffer> <C-k> ``<Left>
  autocmd FileType markdown inoremap <buffer> <C-l> ```<CR><CR>```<Esc>kA
  autocmd FileType markdown autocmd BufWritePost <buffer> execute '!python3 ' . shellescape(s:script_dir . '/build.py')
augroup END
